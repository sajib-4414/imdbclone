// axiosInstance.ts
import axios, { AxiosInstance, AxiosError } from 'axios';
import { NotificationContextProps, ToastType } from './contexts/NotificationContext';
import { NavigateFunction } from 'react-router-dom';

const createAxiosInstance = (navigate:NavigateFunction, notificationHook:NotificationContextProps): AxiosInstance =>{
  const axiosInstance: AxiosInstance = axios.create({
    baseURL: process.env.REACT_API_HOST,
    // Add any default headers or configurations
  });
  axiosInstance.interceptors.response.use(
    (response) => response,
    (error: AxiosError) => {
      if (error.response?.status === 401) {
        // Redirect to login page
        // You can replace '/login' with your actual login page route
        // window.location.replace('/login');
        console.log("called...")
        notificationHook.showNotification('Please login..',{type:ToastType.Error})
        navigate("/login")
      }
      return Promise.reject(error);
    }
  );
  return axiosInstance;
}

export default createAxiosInstance;
