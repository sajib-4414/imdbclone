import { Outlet, useNavigate } from "react-router-dom";
import React, { useEffect } from "react";
import { LoggedInUser } from "../store/features/loginSlice";
import { useAppSelector } from "../store/store";
export const ProtectedRoute:React.FC = () => {
    const navigate = useNavigate();
    const loggedInUser:LoggedInUser = useAppSelector((state) => state.loginUser.loggedInUser);
    useEffect(()=>{
        if (!loggedInUser) {
            navigate("login");
          }
      },[])

    return (
          <Outlet />
    );
  };