import React, { FC, useEffect } from 'react';
import Add from './components/Add';
import List from './components/List';
import { Provider } from 'react-redux';
import { store, useAppDispatch } from './store/store';
import { fetchPerson } from './store/features/personSlice';
import { Products } from './components/Products';
import { Cart } from './components/Cart';
import Container from './common/Container';
import { Route, Routes } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import Login from './components/auth/Login';
import { loadUserFromStorage } from './store/features/loginSlice';
import { ProtectedRoute } from './common/ProtectedRoute';
import Signup from './components/auth/Signup';
import MovieList from './components/Movies-All';

const AppProviderWrapper = () => {

  return (
    // Set context
    <Provider store={store}> 

    {/* // Now App has access to context */}
    <React.StrictMode>
    <App /> 
    </React.StrictMode>
   
      
    </Provider>
  )
}
const App : FC = () => {
  const dispatch = useAppDispatch(); // Works!
  // useEffect(()=>{
  //   dispatch(fetchPerson())
  // })

   useEffect(()=>{
    const storedUser = localStorage.getItem('user');
    if (storedUser) {
      // Dispatch action to restore user data in the Redux store
      dispatch(loadUserFromStorage(JSON.parse(storedUser)));
    }
  },[])
  
  return (
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
      </Routes>
    </Container>
  );
}


export default AppProviderWrapper;
