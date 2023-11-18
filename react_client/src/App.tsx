import React, { FC, useEffect } from 'react';
import Add from './components/Add';
import List from './components/List';
import { Provider } from 'react-redux';
import { store, useAppDispatch } from './store/store';
import { fetchPerson } from './store/features/personSlice';
import { Products } from './components/Products';
import { Cart } from './components/Cart';
import Container from './common/Container';
import { Route, Routes, useNavigate } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import Login from './components/auth/Login';
import { LoggedInUser, loadUserFromStorage, logoutDeleteFromStorage } from './store/features/loginSlice';
import { ProtectedRoute } from './common/ProtectedRoute';
import Signup from './components/auth/Signup';
import MovieList from './components/Movies-All';
import NotFound from './common/NotFound';
import { NotificationProvider, useNotification } from './contexts/NotificationContext';
import createAxiosInstance from './axiosInstance';
import axios, { AxiosResponse } from 'axios';

const AppProviderWrapper = () => {

  return (
    // Set context of React store
    <Provider store={store}> 
    {/* // Now App has access to context */}
        <App /> 
    </Provider>
  )
}
const App : FC = () => {
  const dispatch = useAppDispatch(); // Works!
  // useEffect(()=>{
  //   dispatch(fetchPerson())
  // })
  interface RefreshTokenResponse{
    access_token:string;
    refresh_token:string;
    token_type:string;
  }
   useEffect(()=>{
    const storedUserData = localStorage.getItem('user');
    if (storedUserData) {
      const loggedInUser:LoggedInUser = JSON.parse(storedUserData) as LoggedInUser;
      axios.post('/auth/token/refresh',{
        "refresh_token": loggedInUser.refresh_token
          })
            .then((response: AxiosResponse<RefreshTokenResponse>) => {
              const refreshTokenResponse = response.data;
              loggedInUser.token = refreshTokenResponse.access_token;
              loggedInUser.refresh_token = refreshTokenResponse.refresh_token;
              dispatch(loadUserFromStorage(loggedInUser));
              console.log("token was refreshed")
            })
            .catch(error => {
              console.error('Error refreshing token:', error);
              dispatch(logoutDeleteFromStorage())
            });
    }
  },[])
  
  return (
    <NotificationProvider>
      <Container>
        <Routes>
          <Route path="/" element={ <Dashboard/> } />
          <Route path="login" element={ <Login /> } />
          <Route path="signup" element={ <Signup /> } />
          <Route element={<ProtectedRoute/>}>
            <Route path="add" element={ <Add /> } />
          </Route>
          <Route path="movies" element={ <MovieList /> } />
          <Route path="users" element={ <List /> } />
          <Route path="products" element={ <Products/> } />
          <Route path="cart" element={ <Cart/> } />
          <Route path="*" element={ <NotFound/> } />
        </Routes>
      </Container>
    </NotificationProvider>
    
  );
}


export default AppProviderWrapper;
