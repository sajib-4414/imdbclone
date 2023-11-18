import { Outlet, useNavigate } from "react-router-dom";
import React, { useEffect, useRef } from "react";
import { useAppSelector } from "../store/store";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { useNotification } from "../contexts/NotificationContext";
import { LoggedInUser } from "../interfaces/LoginInterfaces";
export const ProtectedRoute: React.FC = () => {
  const navigate = useNavigate();
  const notificationHook = useNotification();
  const loggedInUser: LoggedInUser = useAppSelector(
    (state) => state.loginUser.loggedInUser,
  );
  const initialized = useRef(false);
  useEffect(() => {
    //checking if it is first render
    if (!initialized.current) {
      initialized.current = true;
      //if first time render, then if not logged in show the toast. Because react was rendering this twice.
      if (!loggedInUser) {
        //check again in local storage,  as state takes time to load
        const storedUser = localStorage.getItem("user");
        if (!storedUser) {
          notificationHook.showNotification("Please login first");
          navigate("login");
        }
      }
    }
  }, []);

  return (
    <>
      <ToastContainer />
      <Outlet />
      {/* outlet renders the child components passed to a protected route if validation passes */}
    </>
  );
};
