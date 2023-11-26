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
- Another issue i found with kafka was, even if i specified user_service depends on kafka, that was not engough. that just means starting of service, not actively listening. therefore userservice which has code to call kafka to send events, was not getting the kafka ready on boot. so i had to add a health check block on the docker compose for kafka, and on the user service, i added condition such as kafka has to be healthy, until then wait for kafka to be healthy before user service starts.
- for now I am copying the grpc codes to both of the producing and listening projects, will move them to a common shared library.
- for now, kafka events code is copied to all the producing and listening projects, will move them to a common shared library.
- in movie service, to start listenign to kafka events, i had so much trouble, i tried creating django management command file to start listening to kafka, and then creating a python file to start a thread with the two process runserver and manage.py [command file name]. It worked but it required creating this thread with 2 workers. also it does to reload if command file is changed.
so then i was looking for another options, then i found out that with the apps.py's ready method i can call the consumer to keep listening. the **shortcoming** is yet, i am not able to reload, if i change the consumer file or any file that consumer is referring to for event handling. in that case i have to restart the movie service, if i change the consumer logic. Also it does not run the django server anymore, just the listener, so switched back to command file mentioned above.


##### Access process.env variables
- use DotEnv with webpack to get access to process.env variables.

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