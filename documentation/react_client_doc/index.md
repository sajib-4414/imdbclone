# React Client

Frontend is built with React, Typescript, Redux toolkit.

<!-- ## means these are Subheadings, will be included in the sphinx home page, ### or more # are not included -->
## Libraries Used

React, Express, React toolkit, nodejs.

### How to enable Redux


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

#### Only frontnend related implementation things:

##### How did I do centralized axios returning to login page if 401 received?
- I created axios instance, and inside I created interceptor to modify requests, response. Interceptor does not have access to the useNavigate or view component access, so 
- I passed useNavigate, useNotificaiton Toast, so that if the response gets 401 it shows the notification, and redirects to login.

##### How to init a typescript project with webpack?
- I followed a medium article, I will add it soon.

##### How add a route guard to make a route protected?
- see the App file and ProtectedRoute file

##### How to add redux toolkit?

##### Format code?
- prettier is installed, format script is added to package.json
- before committing run, `npm run format`

