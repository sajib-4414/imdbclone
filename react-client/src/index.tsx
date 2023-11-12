import 'bootstrap/dist/css/bootstrap.css';
import * as React from 'react';
// import * as ReactDOM from 'react-dom';
import ReactDOM from "react-dom/client";
import App from './App';
import { BrowserRouter } from "react-router-dom";
import '@fortawesome/fontawesome-free/css/all.css';
const root = ReactDOM.createRoot(document.getElementById("root") as HTMLElement);

root.render(
    <React.StrictMode>
       <BrowserRouter>
          <App />
       </BrowserRouter>
    </React.StrictMode>
  );
  