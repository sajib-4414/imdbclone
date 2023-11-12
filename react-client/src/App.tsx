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

const AppProviderWrapper = () => {

  return (
    // Set context
    <Provider store={store}> 

    {/* // Now App has access to context */}
    <App /> 
      
    </Provider>
  )
}
const App : FC = () => {
  const dispatch = useAppDispatch(); // Works!
  useEffect(()=>{
    dispatch(fetchPerson())
  })
  return (
    <Container>
      <Routes>
        <Route path="/" element={ <Dashboard/> } />
        <Route path="login" element={ <Login /> } />
        <Route path="add" element={ <Add /> } />
        <Route path="users" element={ <List /> } />
        <Route path="products" element={ <Products/> } />
        <Route path="cart" element={ <Cart/> } />
      </Routes>
      
      
      
      
    </Container>
  );
}


export default AppProviderWrapper;
