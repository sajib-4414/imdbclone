import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAppDispatch } from "../../store/store";
import { doLogin } from "../../store/features/loginSlice";
import { unwrapResult } from "@reduxjs/toolkit";
import Error from "../../common/Error";
import "react-toastify/dist/ReactToastify.css";
import { ToastType, useNotification } from "../../contexts/NotificationContext";

const Login: React.FC = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const dispatch = useAppDispatch();
  const [loginError, setLoginError] = useState([]);
  const notificationHook = useNotification();

  const submitLogin = async () => {
    if (!loginValidate()) {
      return;
    }
    try {
      const resultAction = await dispatch(doLogin({ username, password }));
      const originalPromiseResult = unwrapResult(resultAction); //is needed to throw error
      // console.log("original promise here")
      // console.log(originalPromiseResult)//you can read succees response here

      // If login is successful, redirect to the home page
      notificationHook.showNotification("Login successful", {
        type: ToastType.Success,
      });
      navigate("/");
    } catch (rejectedValueOrSerializedError) {
      // Handle login error
      setLoginError(rejectedValueOrSerializedError.errors);
      console.error("Login failed:", rejectedValueOrSerializedError.errors);
    }
  };
  const loginValidate = (): boolean => {
    const errors = [];
    switch (true) {
      case !username:
        errors.push({
          error_code: "usename_empty",
          error_details: "Username is required",
        });
      case !password:
        errors.push({
          error_code: "password_empty",
          error_details: "Password is required",
        });
    }
    if (errors.length > 0) {
      setLoginError(errors);
      return false;
    }
    return true;
  };

  return (
    <div className="container mt-5">
      <h2 className="mb-4">Login</h2>
      <form>
        <div className="mb-3">
          <label htmlFor="email" className="form-label">
            Username
          </label>
          <input
            type="text"
            className="form-control"
            id="email"
            placeholder="Enter username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>

        <div className="mb-3">
          <label htmlFor="password" className="form-label">
            Password
          </label>
          <input
            type="password"
            className="form-control"
            id="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        <button type="button" className="btn btn-primary" onClick={submitLogin}>
          Login
        </button>
      </form>
      {loginError.length > 0 && <Error errors={loginError} />}
    </div>
  );
};
export default Login;
