import React, { FC, useEffect } from "react";
import { Provider } from "react-redux";
import Container from "./common/Container";
import { Route, Routes } from "react-router-dom";
import Login from "./components/auth/Login";
import Signup from "./components/auth/Signup";
import { ProtectedRoute } from "./common/ProtectedRoute";
import Dashboard from "./components/Dashboard";
import { store, useAppDispatch } from "./store/store";
import { loadUserFromStorage, logoutDeleteFromStorage } from "./store/features/loginSlice";
import axios, { AxiosResponse } from "axios";
import { LoggedInUser } from "./interfaces/LoginInterfaces";
import { NotificationProvider } from "./contexts/NotificationContext";
import ExportIndex from "./components/export/ExportIndex";
import NotFound from "./common/NotFound";
import UserList from "./components/users/Userlist";
import MovieList from "./components/movies/MovieList";

const AppProviderWrapper = () => {
  return (
    // Set context of React store
    <Provider store={store}>

      {/* // Now App has access to context */}
      <App />

     </Provider>
  );
};
const App: FC = () => {
  const dispatch = useAppDispatch(); // Works!
  interface RefreshTokenResponse {
    access_token: string;
    refresh_token: string;
    token_type: string;
  }
  useEffect(() => {
    const storedUserData = localStorage.getItem("user");
    if (storedUserData) {
      const loggedInUser: LoggedInUser = JSON.parse(
        storedUserData,
      ) as LoggedInUser;
      const tokenRefreshUrl =process.env.REACT_API_HOST + "/auth/token/refresh"
      axios
        .post(tokenRefreshUrl, {
          refresh_token: loggedInUser.refresh_token,
        })
        .then((response: AxiosResponse<RefreshTokenResponse>) => {
          const refreshTokenResponse = response.data;
          loggedInUser.token = refreshTokenResponse.access_token;
          loggedInUser.refresh_token = refreshTokenResponse.refresh_token;
          dispatch(loadUserFromStorage(loggedInUser));
          console.log("token was refreshed");
        })
        .catch((error) => {
          console.error("Error refreshing token:", error);
          dispatch(logoutDeleteFromStorage());
        });
    }
  }, []);

  return (
    <NotificationProvider>
      <Container>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="login" element={<Login />} />
          <Route path="signup" element={<Signup />} />
          <Route element={<ProtectedRoute />}>
            {/* <Route path="add" element={<Add />} /> */}
            <Route path="export" element={<ExportIndex />} />
            <Route path="userlist" element={<UserList />} />
            <Route path="movielist" element={<MovieList />} />
          </Route>
          {/* <Route path="movies" element={<MovieList />} />
          <Route path="users" element={<List />} />
          <Route path="products" element={<Products />} />
          <Route path="cart" element={<Cart />} /> */}
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Container>
     </NotificationProvider>
  );
};

export default AppProviderWrapper;
