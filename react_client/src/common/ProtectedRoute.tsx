import { Outlet, useNavigate } from "react-router-dom";
import React, { useEffect, useRef, useState } from "react";
import { LoggedInUser } from "../store/features/loginSlice";
import { useAppSelector } from "../store/store";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
export const ProtectedRoute:React.FC = () => {
    const navigate = useNavigate();
    const loggedInUser:LoggedInUser = useAppSelector((state) => state.loginUser.loggedInUser);
    var toastDisplayed = false;
    useEffect(()=>
    {
      if(!loggedInUser)
      {
        //check again in local storage,  as state takes time to load
        const storedUser = localStorage.getItem('user');
        if(!storedUser && !toastDisplayed)
        {
          toast.error('Login first',{
            position: "top-center"
          });
          toastDisplayed = true;
          setTimeout(() => {
            navigate("login");   
          }, 1500); 
          
        }
      }
    },[])

    return (
          <>
          <ToastContainer />
          <Outlet />
          {/* outlet renders the child components passed to a protected route if validation passes */}
          </>
          
    );
  };