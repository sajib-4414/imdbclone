// axiosInstance.ts
import axios, { AxiosInstance, AxiosError } from 'axios';

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
      window.location.replace('/login');
    }
    return Promise.reject(error);
  }
);

export default axiosInstance;
