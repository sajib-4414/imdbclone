import { createAsyncThunk, createSlice, PayloadAction } from "@reduxjs/toolkit";
import axios from "axios";
export interface LoggedInUser{
    id: number;
    // name: string; will be brought soon
	email:string; 
	username:string;
	token:string
}

export interface LoggedInUserState{
	loggedInUser: LoggedInUser | null;
}

const initialState:LoggedInUserState={
	loggedInUser: null
}

//unique key, async function
// export const doLogin = createAsyncThunk(
// 	"user/login", 
// 	async({ username, password }: { username: string; password: string }, thunkAPI)=>
// 	{
// 		const root_url = "http://localhost:8005" //process.env.REACT_API_HOST
// 		const loginUrl = `${root_url}/auth/login`
// 		try{
// 			const response = await fetch(loginUrl , {
// 				method: "POST",
// 				headers:{
// 					"Content-Type": "application/json"
// 				},
// 				body:JSON.stringify({
// 					username,
// 					password
// 				})
// 			})
// 			if (!response.ok) {
// 				if (response.status === 401) {
// 				  // Handle 401 Unauthorized error
// 				  console.error("Unauthorized access:", response.statusText);
// 				  return thunkAPI.rejectWithValue("Unauthorized access");
// 				}
		
// 				// Handle other HTTP errors
// 				const errorData = await response.json();
// 				throw new Error(errorData.message);
// 			}
// 			const data = await response.json();//data will have name and id inside it
// 			return data;
// 		} catch(err){
// 			if (!err.response) {
// 				throw err
// 			  }
			
// 			//throw error
// 			return thunkAPI.rejectWithValue(err.message)
// 			//return rejectWithValue(err.response.data)
// 		}
// 	}
// )	

export const doLogin = createAsyncThunk(
	"user/login",
	async ({ username, password }: { username: string; password: string }, thunkAPI) => {
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
	}
  );

export const LoginSlice = createSlice({
	name:"loginstate",
	initialState,
	reducers:{
	
	},
	extraReducers:(builder)=>{
		//every asynchtyunk retyurns 3 state, the async function with thumnk
        //first state is fulfilled with is no error,  second state is loading state when async
        //funciton is not yet resolved, third one is error state, when async fncitn inside thunk returns error
		builder.addCase(doLogin.fulfilled,(state,action)=>{
            //action has the response payload
            state.loggedInUser = action.payload
			console.log("action payload is")
			console.log(state.loggedInUser.token)
        })
		builder.addCase(doLogin.rejected, (state, action) => {
			state.loggedInUser = null;
			// state.error = action.error.message || "Login failed."; // Set error message
		});
	}
})	

export default LoginSlice.reducer;
