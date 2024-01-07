# React Client

Frontend is built with React, Typescript, Redux toolkit.

<!-- ## means these are Subheadings, will be included in the sphinx home page, ### or more # are not included -->
## Libraries Used

React, Express, React toolkit, nodejs.

### How to enable Redux

- Feature 1: Describe feature 1.
- Feature 2: Describe feature 2.
- Feature 3: Describe feature 3.

### Concepts:
- **Use effect**: To run some functions once, or every time some state changes. if the dependency in the dependency array changes, the function will run. if the dependency array is empty, it will run after component rendered for the first time, for once ONLY. Can optionally be used to cleanup unmounting, have to use this feature.
- **Redux toolkit**: To efficiently emit/dispatch events to update state of the app centrally, and get the state centrally.
- **Scoped styling**: Used emotion styled component for scoped styling. We first create a Container with the css, and then create the actual component with the container component. Example found in Movies-All.tsx. Emotion styling can be done with emotion/style or emotion/css. emotion/style has built in typescript support. emotion/css, needs to be configured, it does not easily support typescript.
- **Using Context with Provider For Global task** - used to show notification.
- **using centralized axios instance** - used an axios instance. usenavigate, usenotification is passed, so axios can throw
notificaiton and error
- **Typescript with babel** -webpack dev server.
- **token refresh** - on the App component load[triggered by page reloading or first time loading], token is refreshed from API, if token cannot be refreshed, then
state is cleared showing user is not logged in.

#### Findings:
- for some unknown reason, in the react docker file if the directory is /app, then nothing installs, therfore
i set the working directory as /app2
- My react client was was not working without the node_modules on the host, and doing hot reload,
becauase of some problem with docker compose volume mapping. volume mapping replaces the app directory
contents, and the app does not have access to packages installed. https://stackoverflow.com/questions/30043872/docker-compose-node-modules-not-present-in-a-volume-after-npm-install-succeeds . Indeed this is a complex problem, having hot reload, having vscode sugestion, and also not copying host node_modules to the container. This is yet to solve.
- Another issue i found with kafka was, even if i specified user_service depends on kafka, that was not engough. that just means starting of service, not actively listening. therefore userservice which has code to call kafka to send events, was not getting the kafka ready on boot. so i had to add a health check block on the docker compose for kafka, and on the user service, i added condition such as kafka has to be healthy, until then wait for kafka to be healthy before user service starts. Such health check is also necessary for postgres as well. just depends on is not enough.
- for now I am copying the grpc codes to both of the producing and listening projects, will move them to a common shared library.
- for now, kafka events code is copied to all the producing and listening projects, will move them to a common shared library.
- in movie service, to start listenign to kafka events, i had so much trouble, i tried creating django management command file to start listening to kafka, and then creating a python file to start a thread with the two process runserver and manage.py [command file name]. It worked but it required creating this thread with 2 workers. also it does to reload if command file is changed.
so then i was looking for another options, then i found out that with the apps.py's ready method i can call the consumer to keep listening. the **shortcoming** is yet, i am not able to reload, if i change the consumer file or any file that consumer is referring to for event handling. in that case i have to restart the movie service, if i change the consumer logic. Also it does not run the django server anymore, just the listener, so switched back to command file mentioned above.
I also tried with supervisord to run both, but in that case it does not print to terminal anymore, and i think file change is not reflected.
Actually, there is a solution for the kafka, celery workers, grpc server, i can just create anotherr container from the same space in the docker compose, but the running command will be different. i can have one consumer saying kafka consumer, one consumer saying celery run.
- fastapi with postgres, https://testdriven.io/blog/fastapi-docker-traefik/
environment variable passing did not work, and also postgres volume creation did not, had to do a ./
- unwrap result if not called, does not throw the error in the component where i am calling async thunk,
if i want to catch the api call error in the async thunk in the component i am calling from, i need to unwrap, this will give me the raw resultr and also throw exception if there is any.
found in signup.tsx
`doSignUp({
          username: formData["username"],
          password: formData["password"],
          password2: formData["confirmPassword"],
          email: formData["email"],
        }),
      );
      const originalPromiseResult = unwrapResult(resultAction); //is needed to throw error`
-sqlalchemy, ormar using fastapi, i found that i cannot just add a unique not null value in the database
suddenly in a talbe with data, it will show error, that because that column is new, when trying to fill this with null, it gets the eeror that column is not nullable. nullable=False, the lesson is when a table is up and running, with data. make sure a unique non null column has a default value. 
- Migrating sqlite to postgres in User service: Mostly followed this: https://medium.com/djangotube/django-sqlite-to-postgresql-database-migration-e3c1f76711e1 First i took the backup of sqlite, i did this, python manage.py dumpdata > whole.json. Now i added postgres image to docker compose, specified volume, specified db username, password. i also added service healthy check. i then added the postgres db as depends on with healthcheck check to user service. Now i went to django settings, added the postgres settings. Now i added psycopg2 driver as pip install. Now i stopped the containers, and ran docker compose up --build, it built the containers, now i ran the migrations[tutorial said delete migrations, but i did not, i think its not needed], then i deleted content types. now i loaded the data as fixture by going to the shell. **Interesting Observation**, as user was creating user, it was emitting events that user created, but the movie service already have those users, so i saw logs that discarding message, user is already on the movie service. this is a great property of event driven, anytime you are creating the users again maybe for new database, it will again emit events that, and other service as they have the user already discarded it. 
- how i changed auth user model in user service, even after having data. so i added a custom user model, and added it in the settings. now when i did makemgirations, migrete, it was erropring out that migration cannot run, the auth user model change has to be first migration. so took a data dump with dump command in a json file. delete the database, ran the migration[also deleted content types seeing the medium article aboce], it ran successfully. then i imported the data from the json as a fixture. BUT i modifed the user model with current_app.user [i saw the database and json file to see what was before and what need to be changed, before was auth.user now its user_app.user] before importing. **Intertesting** I also found sqlite ddoes not impose strictly the character limit in the models specified, but postgres does. when i was importing thes qlite data dump to postgres, i got error that, limit exceeded. chatgpt said,The error you're encountering suggests a difference in behavior between SQLite and PostgreSQL regarding character varying length constraints. PostgreSQL enforces length constraints more strictly than SQLite, and it appears that a value exceeding the maximum length for a column is causing the issue during the import.
- had issue of data inconsistency, user service created user and passed message, movie service
when tried to create user, exception happened and user not created.
- had data inconsistency, i had identical User with Role, if user role is changed in user service, and it is not yet
processed by the movie service, that is inconsistent data. also if movie service changes the user role, and user service does not, its a consistency problem. data has to be in sync.
- **problem solve story**: [office story bolbo] age synchronously api call e csv generate kortam, lag hoito, tasara djangio single threaded so eta server k block rakhto, pore ami research kore background job e celery dei. ejonno amar model banano lagse track rakhte, storage rakha lagse save korte, ar system ta change kora lagse, request=queued. download api te click korle either file or statusqueued asbe ekhon,
- **problem solve story**: [office story] age JWT diye sob jinis send kora hoto, ete kore, bivinno type er user, bivinno jinis access kora lage ei logic repeat kora lagto bivinno service e. then central permission system banaisi user service e, permission group banaisi bivinno user er jonno, user k business logic er upor vitti kore bivinno group e add kora hoto, like Content Editor user, take content editor group e add kore disi, ekhon query korle user service e kono ekta permission string diye, [permission string gula common pypi package e deya silo], user service bole dito user er ei permisison ase naki, user oi group theke inherit kore permisison peye jay. ar eta sudhu admin side e besi lagse, user side e tmn na, besirvag api open for all consumers, only some apis are open for pro consumers. 
so the individuald services has a copy of users from the event message passing.
consumer side: 
* calls a private api that requires specific permission -> calls the user service to know if the permission exists on user(via permission group).
* calls a private api that is open to all consumers -> just checks the user roles, if the user role in the user copy of the that service says it is a consumer role, then allow access.
* same goes for staff side, some apis are open to all staff's, some apis require specific permission, for them we call to user service. 
- django cors error when serving api via ngix, frotned was localhost:3003, backends were served through nginx. to solve that i had to add cors header conf in nginx conf ONLY, adding in django did not help. also adding in django+nginx also did not work. it said multiple cors headers.

I also used a proxy model, RegularUser, StaffUser, this allows to set the role automatically if you create user with theese proxy models, these are just a virtual copy of regular user model i createad as a custom.
i have two endpoint for two kind of user creation, login, such that those two kind of user objects are created, so that the user is created with roles. also i have a profile for both of them, profiles are created with signal, as soon as user is created. they also send message to kafka.

##### Access process.env variables
- use DotEnv with webpack to get access to process.env variables.
- react js hotload socket not working with nginx config? 
#below code is for accepting websocket connections from react app container, for hotload
            proxy_set_header HOST $host;
            proxy_set_header X-Forwarded-Host $http_host;

            proxy_set_header Upgrade $http_upgrade;
            proxy_http_version 1.1;
            proxy_set_header Connection "upgrade";
            proxy_read_timeout 86400;

##### useeffect is called twice even if dependecies are empty?
- Tried removing strictmode, did not work
- Did this workaround from stackoverflow. to allow useeffect to run exactly once, use it with useref. used it for notification.

  ``const initialized = useRef(false);
  useEffect(()=>{
    if (!initialized.current) {
      initialized.current = true
      doSomethingThatneedstobedneonce()
    }``

##### How Did I do jwt token refresh and prevent stale logged in user?
- In the App component, first check if user exists on local storage, if it does not exist, then dont refresh.
- If user exists in the local storage, then I called the token refresh api to get a new access token and refresh token
- I then stored it to the local storage, also to state via redux reducers.

##### How did I do centralized Toast notification?
- I created a context, and context provider. Then wrapped the container component (inside App) with context provider
- Now the context provider makes a method show notificaition available to all the components, just like React provider
makes available React store to all components.

##### How did I do centralized axios returning to login page if 401 received?
- I created axios instance, and inside I created interceptor to modify requests, response, and what to do
- I passed useNavigate, useNotificaiton Toast, so that if the response gets 401 it shows the notification, and redirects to login.

##### How to init a typescript project with webpack?
- I followed a medium article, I will add it soon.

##### How add a route guard to make a route protected?
- see the App file and ProtectedRoute file

##### How to add redux toolkit?

##### Format code?
- prettier is installed, format script is added to package.json
- before committing run, `npm run format`

##### Integrating Kafka
- user service with signal fires kafka events.
- movie service with consumer catches those events.
- so with kafka if you dont commit messages you will read them from the latest, previous messages will be missed, in case the consumer was down. to handle it, you may choose to always read from the earliest, but in this way you might haave to reprocess a lot of messages that has been seen. so you can auto commit/manual commit each messages, and next time choose to read from the earliest non committed messages. this answer does this,
https://stackoverflow.com/a/51801372/5719810 this ensures you read all messages and commit automatically, and if the consumer was down, and come back up, it will read from its own last committed offset. 
in kafka, every consumer can commit an offset, then they can choose to read from the last committed offset, or read from the earliest. in microservice environment, we often want to read from the last non acknowledged message, so we commit it.
by default kakfa python i think does not commit.  but default implementation will read message from current and not previous. in kafka, you can have one or more consumer in a consumer group, and if a consumer is in a consumer group, then they can commit offset. if you have more than one consuemrr in a group, then kafka will assign different parition to different consumers. and these consumers in a group will commit to different partitions. but if you want multiple microservices to listen to same event and has their own offset, then create unique consumer groups with all those consumers. i have tried this. in the kafka-youtube example code, i am listening to the same topic with transaction.py and test-transaction-2.py file, but i assigned them to unique groups, i can see they can offset on their own, and maintain the last read message successfully individually.
- Experienced single point of failure with the auth service having invoked for all requests. my auth service was
validating jwt token and sending the user inside the jwt, when the auth service was not responding, then the whole application was unusable.
