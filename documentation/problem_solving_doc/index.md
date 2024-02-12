# Problem solution stories & Issues solutions

## Issues solutions
- **Enabling react hotload without copying node modules to docker compose**: 

    *Attempt 1 Without mapping the node_modules to docker*: for some unknown reason, in the react docker file if the directory is /app, then nothing installs, therfore i set the working directory as /app2. While it does the job, but it does not do hotload. React client was was not hot loading without the node_modules on the host, and doing hot reload, becauase of some problem with docker compose volume mapping. volume mapping replaces the app directory contents, and the app does not have access to packages installed. https://stackoverflow.com/questions/30043872/docker-compose-node-modules-not-present-in-a-volume-after-npm-install-succeeds . Indeed this is a complex problem, having hot reload, having vscode sugestion, and also not copying host node_modules to the container. This is yet to solve.
    
    *Attempt2 solution for now, copy the node_modules via volume to docker container for dev*: So i decided for development I will have the volume mapping. And for production i will do NPM CI with the packagelock file, with no node_modules copying, as we dont need hot loading.

- **Data inconsistency**: had data inconsistency, i had identical User with Role, if user role is changed in user service, and it is not yet processed by the movie service, that is inconsistent data. also if movie service changes the user role, and user service does not, its a consistency problem. data has to be in sync. Couple of ways has been done, services are put in different kafka group so that they can retry, certain logics are handled in just one service, and other services synchronously call that service. Still not fully solved. maybe we can do SAGA pattern like the nodejs project.
- **CORS header problem**: django cors error when serving api via ngix, frotned was localhost:3003, backends were served through nginx. to solve that i had to add cors header conf in nginx conf ONLY, adding in django did not help. also adding in django+nginx also did not work. it said multiple cors headers.
- **useeffect is called twice even if dependecies are empty?**
    - Attempt1-> Tried removing strictmode, did not work
    - Attempt2-> Did this workaround from stackoverflow. Using useRef to track if its first time rendering or not, so we only render one time. to allow useeffect to run exactly once, use it with useref. used it for notification.

  ``const initialized = useRef(false);
  useEffect(()=>{
    if (!initialized.current) {
      initialized.current = true
      doSomethingThatneedstobedneonce()
    }``
- **Enabling hotload of react App with nginx**: react js hotload socket not working with nginx config, then i upgraded the header with this config to allow socket connections for hotloading of the react app.
```
#below code is for accepting websocket connections from react app container, for hotload
proxy_set_header HOST $host;
proxy_set_header X-Forwarded-Host $http_host;

proxy_set_header Upgrade $http_upgrade;
proxy_http_version 1.1;
proxy_set_header Connection "upgrade";
proxy_read_timeout 86400;
```
- **Access process.env variables in App+webpack config**: use DotEnv with webpack to get access to process.env variables.
- **fastapi with postgres, Pyndatic env variable did not work, used os.getenv**, https://testdriven.io/blog/fastapi-docker-traefik/. Parsing the encironment variavle with pyndatic did not work, used os.getenv
- **volume declaration issue**: in the docker compose file volume section, just writing the volume name did not work, had to add a ./ like `./postgres_volume`instead of `postgres_volume`

## Specific Problem solution stories
- **Improvement of Export service - Asynchronous report generation+precompute with Celery beat**: 
    - [office story bolbo] We had an export fuinctionality on the staff side, so everytime a staff user would click export it would synchronously call API and generate the CSV right away. As the data volume grew it started to take higher time, lagging and as django is single threaded, therefore it would block the server. 
    - I did some research, and then implemented asyncrhonous celery based worker to generate the CSV files. So I created a Model to keep track of the export, what is the status, if the status is done which will be set by the celery worker, that means file is now on the server, and i created a HTTP streaming download link to download the CSV. If the file is not yet done processing, thge status of the export would be request=queued. So loading the export page will say the export status is either done or queued or in process. 
    - Also I noticed that certain data could be precomputed, who make the exports faster, therefore i also installed celery beat that set a crontab to run the some celery jobs to precompute some data, that the stakeholders in the staff side often need for the exports.
- **Implementing centralized Role Based access control**: [office story] age JWT diye sob jinis send kora hoto, ete kore, bivinno type er user, bivinno jinis access kora lage ei logic repeat kora lagto bivinno service e. then central permission system banaisi user service e, permission group banaisi bivinno user er jonno, user k business logic er upor vitti kore bivinno group e add kora hoto, like Content Editor user, take content editor group e add kore disi, ekhon query korle user service e kono ekta permission string diye, [permission string gula common pypi package e deya silo], user service bole dito user er ei permisison ase naki, user oi group theke inherit kore permisison peye jay. ar eta sudhu admin side e besi lagse, user side e tmn na, besirvag api open for all consumers, only some apis are open for pro consumers. 
so the individuald services has a copy of users from the event message passing.
consumer side: 
* calls a private api that requires specific permission -> calls the user service to know if the permission exists on user(via permission group). It also caches the permission response for 15 minutes.
* calls a public api that is open to all consumers -> just checks the user roles, if the user role in the user copy of the that service says it is a consumer role, then allow access.
* same goes for staff side, some apis are open to all staff's, some apis require specific permission, for them we call to user service. caches the permission for 15 minutes.
- **Creating different type of users based on set business logic with Proxy Model**: I also used a proxy model, RegularUser, StaffUser, this allows to set the role automatically if you create user with theese proxy models, these are just a virtual copy of regular user model i createad as a custom. You can add some logic that Using Proxy Model A means, it will create an Object of Main Model, plus some data will be set that are specific to A. For example, RegularUser is a Proxy Model of User, so it creates the User model and also set the user role to regular. so the code was more manageable. for example, admin has access to admin panel user settings yes, but the staff level1 doesnot have the access to user settings, No. staff level2 has access to notifications. so this kind of Role based Access Controls.
i have two endpoint for two kind of user creation, login, such that those two kind of user objects are created, so that the user is created with roles. also i have a profile for both of them, profiles are created with signal, as soon as user is created. they also send message to kafka.
- **Single point of failure**: Experienced single point of failure with the auth service having invoked for all requests. The auth service was doing jwt token generation and verificatin. my auth service was validating jwt token and sending the user inside the jwt, when the auth service was not responding, then the whole application was unusable. [to tell in interview] to solve this, i added the jwt parsing capability as a PyPi library, and added that in other projects.
- **Depending on kafka healthchk instead of just depends on**: i found with kafka was, even if i specified user_service depends on kafka, that was not engough. that just means starting of service, not actively listening. therefore userservice which has code to call kafka to send events, was not getting the kafka ready on boot. so i had to add a health check block on the docker compose for kafka, and on the user service, i added condition such as kafka has to be healthy, until then wait for kafka to be healthy before user service starts. Such health check is also necessary for postgres as well. just depends on is not enough.
- **GRPC files needed for both producer and consumer, therefore I moved to PyPi package as a result** for now I am copying the grpc codes to both of the producing and listening projects, will move them to a common shared library.[for interview] I moved them to a PyPi package, now I install and use them both in the listener and producer.
- **Running Kafka listener/Celery/RabbitMQ and HTTP server at the same time, created a shared container**: in movie service, to start listenign to kafka events, i had so much trouble.

    *Attempt 1 creating django management command and run in different thread* : i tried creating django management command file to start listening to kafka, and then creating a python file to start a thread with the two process, one is runserver(http server) and manage.py [command file name]. It worked but it required creating this thread with 2 workers. also it does reload if command file is changed.
    
    *Attempt 2 using the django ready method in admin.py*: so then i was looking for another options, then i found out that with the apps.py's ready method i can call the consumer to keep listening. the problem is the listener blocks the thread, django can no longer listen to HTTP traffic. 

    *Attempt 3 with sueprvisord*: I also tried with supervisord to run both, but in that case it does not print to terminal anymore, and i think file change is not reflected.

    *Attempt4 with shared container*: Actually, there is a solution for the kafka, celery workers, grpc server, i can just create anotherr container from the same space in the docker compose, but the running command will be different. i can have one consumer saying kafka consumer, one consumer saying celery run.

- **Frotnend: Catching the exception that happened inside react redux with unwrap result**: Normally if there is exception occurred in redux async thunk api call, it calls the rejected part of the async thunk, but if I want to catch the error in the calling component, then i need to use unwrap result. this will give me the raw resultr and also throw exception if there is any.
found in signup.tsx
```
doSignUp({
          username: formData["username"],
          password: formData["password"],
          password2: formData["confirmPassword"],
          email: formData["email"],
        }),
      );
      const originalPromiseResult = unwrapResult(resultAction); //is needed to throw error
```
- **A new column in SQL database (when it already has data), cannot be unique not null without a default value, and it must have default value for existing rows**:
sqlalchemy, ormar using fastapi, i found that i cannot just add a unique not null value in the database
suddenly in a talbe with data, it will show error, that because that column is new, when trying to fill this with null, it gets the eeror that column is not nullable. nullable=False, the lesson is when a table is up and running, with data. make sure a unique non null column has a default value. 
- **Mgirating from SQLITE to Postgres**: Mostly followed this: https://medium.com/djangotube/django-sqlite-to-postgresql-database-migration-e3c1f76711e1 

    -  First i took the backup of sqlite, i did this, `python manage.py dumpdata > whole.json`. 
    
    - Now i added postgres image to docker compose, specified volume, specified db username, password.
    
    - I also added `service healthy` check. i then added the postgres db as *depends on with healthcheck check* to user service. 
    - Now i went to django settings, added the postgres driver related settings. 
    - Now i added `psycopg2` driver as pip install. 
    - Now i stopped the containers, and ran docker compose up --build, it built the containers,
    - now i ran the migrations[tutorial said delete migrations, but i did not, i think its not needed], then i deleted content types. 
    - now i loaded the data as fixture by going to the shell. 
    
    **Observation: User creaton Events discarded when creating users loading the fixture**, as user was creating user, it was emitting events that user created, but the movie service already have those users, so i saw logs that discarding message, user is already on the movie service. this is a great property of event driven, anytime you are creating the users again maybe for new database, it will again emit events that, and other service as they have the user already discarded it. 
- **Changing the Auth User Model later in the project**: how i changed auth user model in user service, even after having data. 
    - so i added a custom user model, and added it in the settings. now when i did makemgirations, migrete, it was erroring out that migration cannot run, the auth user model change has to be first migration. 
    - so took a data dump with dump command in a json file. 
    - delete the database, ran the migration[also deleted content types seeing the medium article aboce], it ran successfully. 
    - then i imported the data from the json as a fixture. BUT i modifed the user model with current_app.user [i saw the database and json file to see what was before and what need to be changed, before was auth.user now its user_app.user] before importing. 
    - **SQlite doesnt impose character limit strictly** I also found sqlite does not impose strictly the character limit in the models specified, but postgres does. when i was importing thes sqlite data dump to postgres, i got error that, limit exceeded. chatgpt said,The error you're encountering suggests a difference in behavior between SQLite and PostgreSQL regarding character varying length constraints. *PostgreSQL enforces length constraints more strictly than SQLite*, and it appears that a value exceeding the maximum length for a column is causing the issue during the import.
- **message missing problem with Kafka, solution respective group and manual ack after message process done:** had issue of data inconsistency, user service created user and passed message, movie service when tried to create user, exception happened and user not created. To solve this, I added the services such as movie, notificaiton who each need to track the message read, in different groups. from chatgpt, each consumer group maintains its own offset for each partition it consumes from. This means that if you have two consumer groups, one for the message service and another for the movie service, they will maintain separate offsets based on their respective commits.
- **Frotnend: Refreshing the token to prevent stale JWT token+ stale logged in State in the frotnend**:
    - In the App component, which is triggered if webpage is relaoded, first check if user exists on local storage, if it does not exist, means the user is not logged in, then dont refresh.
    - If user exists in the local storage, then I called the token refresh api to get a new access token and refresh token. If I see it fails that means the token is corrupted, so it logout the user in the storage and also the state. If refreshing token succeeeds, I then stored it to the local storage, also to state via redux reducers.
- **Frotnend: How did I do centralized Toast notification?**
    - I created a context, and context provider. Then wrapped the container component (inside App) with context provider
    - Now the context provider makes a method show notificaition available to all the components, just like React provider makes available React store to all components.
- **Kafka When to use Group and how consumers work in a consumer group**:
    - Process flow: user service with signal fires kafka events. movie service with consumer catches those events.
    - *Enabling Ack +unique group to read the messages if not acknowed*: so with kafka if you dont commit messages you will read them from the latest, previous messages will be missed, in case the consumer was down. to handle it, you may choose to always read from the earliest, but in this way you might haave to reprocess a lot of messages that has been seen. so you can auto commit/manual commit each messages, and next time choose to read from the earliest non committed messages. this answer does this, https://stackoverflow.com/a/51801372/5719810 this ensures you read all messages and commit automatically, and if the consumer was down, and come back up, it will read from its own last committed offset. in kafka, every consumer can commit an offset, then they can choose to read from the last committed offset, or read from the earliest. in microservice environment, we often want to read from the last non acknowledged message, so we commit it. by default kakfa python i think does not commit.  but default implementation will read message from current and not previous. in kafka, you can have one or more consumer in a consumer group, and if a consumer is in a consumer group, then they can commit offset. if you have more than one consuemrr in a group, then kafka will assign different parition to different consumers. and these consumers in a group will commit to different partitions. but if you want multiple microservices to listen to same event and has their own offset, then create unique consumer groups with all those consumers. i have tried this. in the kafka-youtube example code, i am listening to the same topic with transaction.py and test-transaction-2.py file, but i assigned them to unique groups, i can see they can offset on their own, and maintain the last read message successfully individually.
- **TODO:what to do in case a message is missed**: maybe do a compensating transaction. chatgpt bolse cleery timer diya rakhte pari
## Database ORM query optimization:
- **Optimization with index**:in the movie service, first i had a test run to create 100k movies, and then lookup movies in 50k-51k range based on the titles. i logged the time with datetime.now before and after. i saw that query took 7s for lookup. Then i created an index on the title. now i again ran the test, i saw lookup time reduced to 0.79s.
- **bulk query**: in the test method i created 100k movies with a for loop, one by one. it took whopping 53s. to optimize this, i then used the bulk_create method with 500 batch size, 100k movie creation took 7s.

  According to Django’s documentation, performing a database lookup using a field that has unique=True or db_index=True (like id or title field) will be faster than using a non-indexed field like author in our Article model above.
  Note that id fields are automatically indexed by Django.

- **Avoiding N+1 Queries with `select_related`:**
  When retrieving foreign key objects, use `select_related` to perform an SQL join and fetch related data at the same time, which is more efficient when you need both the main object and the nested/foreign key object frequently. 
  
  If you do ``movie = Movie.objects.get(pk=1)`` and then ``platform_name = movie.platform.name``, it first just queries the databse for a movie, and when you want the platform_name, it again quyeries the database for platform with the foreign key relationship. This means two trip to the database, and it could be costly if you always need the platform object. 
  
  In this case it is better to do a `select_related `which will do a join between these two tables and fetch the platform and the movie at the same time with one trip.
  
  I tested, with 100k retrieval in the movie service tests, without select related it takes 2.5minutes, with select_related it takes 1.75 minutes. which is a huge gain of 30%.
  Example:
  ```python
  movie = Movie.objects.select_related("platform").get(pk=1)
  platform_name = movie.platform.name
  ```
  `select_related` works for one to one or one to many relations.

- **Using prefetch related**: Using prefetch_related()
from orely media -> `select_related()` will help you boost performance for retrieving related objects in one-to-many relationships. However, select_related() cannot work for many-to-many or many-to-one relationships (ManyToMany or reverse ForeignKey fields). Django offers a different QuerySet method called prefetch_related that works for many-to-many and many-to-one relations in addition to the relations supported by `select_related()`. The `prefetch_related()` method performs a separate lookup for each relationship and joins the results using Python. This method also supports the prefetching of GenericRelation and GenericForeignKey.

    In the movie service, i have streaming platforms, each movie is associated with a streanming platform. So a streaming plaform can have multiple movies. so from movie to streaming platform it is many to one, and from streaming to movie its one to many. So i tried prefetch related from a streaming platform to find movies with associated with it. I tried retrieving the movies 1000k time witout prefetch_related and 1000k time with prefetch_related, i saw significcant gain. without fetch related it was 24s. with prefetch related it was 3s. therefor it is 88% faster.

- **Using defer to defer loading properties**: In django we can use ``defer`` to defer loading some properties that we may not need right now or dont need at all in certain contexts. deferring the load/query of some properties can speed up the query. in the movie service i wrote a test, where i deferred loading of storyline and platform when querying the movie, i did that in a loop for 10k time, i saw that without defer the query time was 7.46s, with defer the query time was 6.52s. which means 13% almost gain. i ran the query like this `Movie.objects.defer("storyline", "platform").get(title="Movie title1")` . Also similar way how we can use defer, we can use the reverse of defer which is only, if you specify only some properties of an object, it will also make the query faster. `Movie.objects.only("platform")`

- **Using count instead of len for counting queryset**:
When you use len() on a queryset, Django first fetches all the records in the queryset from the database into memory, and then Python's len() function is applied to the resulting list. This means that len() retrieves all the data from the database, which can be extremely slow and memory-intensive for large datasets. Using count() the counting is done in the database and the data isn’t fetched and evaluated. so count does this, `SELECT COUNT(*) FROM article;` which is way faster retrieving everything and count them later.

    I tested doing the moviue count for 100k times, and i saw that having a len(queryset) is slower, and `Movie.objects.all().count()` was faster. without count it took 57s, and with count it took 41s, which is 37% faster.
- Not using order_by if not needed, at it slows down the query by 10-20%.

