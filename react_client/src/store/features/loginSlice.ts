import { createAsyncThunk, createSlice, PayloadAction } from "@reduxjs/toolkit";
import axios from "axios";
import {
  LoggedInUser,
  LoggedInUserState,
} from "../../interfaces/LoginInterfaces";

const initialState: LoggedInUserState = {
  loggedInUser: null,
};

//unique key, async function
export const doLogin = createAsyncThunk(
  "user/login",
  async (
    { username, password }: { username: string; password: string },
    thunkAPI,
  ) => {
    const root_url = "http://localhost:8005"; // process.env.REACT_API_HOST
    const loginUrl = `${root_url}/auth/login`;

    try {
      const response = await axios.post(loginUrl, {
        username,
        password,
      });

      return response.data;
    } catch (err) {
      // Axios automatically rejects the promise on HTTP error status codes
      if (axios.isAxiosError(err)) {
        const status = err.response?.status;

        //   if (status === 401) {
        // 	// Handle 401 Unauthorized error
        // 	console.error("Unauthorized access:", err.response?.data);
        // 	return thunkAPI.rejectWithValue("Unauthorized access");
        //   }

        // Handle other HTTP errors
        console.error("HTTP error:", err.response?.data);
        return thunkAPI.rejectWithValue(err.response?.data);
      }

      // // Handle network errors and other issues
      // console.error("Login failed:", err);
      // return thunkAPI.rejectWithValue(err);
    }
  },
);

export const doSignUp = createAsyncThunk(
  "user/signup",
  async (
    {
      username,
      password,
      password2,
      email,
    }: { username: string; password: string; password2: string; email: string },
    thunkAPI,
  ) => {
    const root_url = process.env.REACT_API_HOST; //  "http://localhost:8005";
    const loginUrl = `${root_url}/user-service/api/v1/account/register/`;

    try {
      const response = await axios.post(loginUrl, {
        username,
        password,
        password2,
        email,
      });

      return response.data;
    } catch (err) {
      // Axios automatically rejects the promise on HTTP error status codes
      if (axios.isAxiosError(err)) {
        // Handle other HTTP errors
        console.error("HTTP error:", err.response?.data);
        return thunkAPI.rejectWithValue(err.response?.data);
      }
    }
  },
);

export const LoginSlice = createSlice({
  name: "loginstate",
  initialState,
  //this section is synchronous redux
  reducers: {
    loadUserFromStorage: (state, action: PayloadAction<LoggedInUser>) => {
      state.loggedInUser = action.payload;
    },
    logoutDeleteFromStorage: (state, action: PayloadAction) => {
      state.loggedInUser = null;
      localStorage.removeItem("user");
    },
  },
  //this section is for async thunk redux
  extraReducers: (builder) => {
    //every asynchtyunk retyurns 3 state, the async function with thumnk
    //first state is fulfilled with is no error,  second state is loading state when async
    //funciton is not yet resolved, third one is error state, when async fncitn inside thunk returns error
    builder.addCase(doLogin.fulfilled, (state, action) => {
      //action has the response payload
      state.loggedInUser = action.payload; //storing the logged in user in the state
      localStorage.setItem("user", JSON.stringify(action.payload));
    });
    builder.addCase(doLogin.rejected, (state, action) => {
      state.loggedInUser = null;
    });
    builder.addCase(doSignUp.fulfilled, (state, action) => {
      //action has the response payload
      state.loggedInUser = action.payload; //storing the logged in user in the state
      localStorage.setItem("user", JSON.stringify(action.payload));
    });
    builder.addCase(doSignUp.rejected, (state, action) => {
      state.loggedInUser = null;
    });
  },
});

//this exports extra reducers automatically
export default LoginSlice.reducer;
//this exports regular reducers
export const { loadUserFromStorage, logoutDeleteFromStorage } =
  LoginSlice.actions;
