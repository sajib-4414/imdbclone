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
	//this section is synchronous redux
	reducers:{
		loadUserFromStorage:(state, action:PayloadAction<LoggedInUser>)=>{
            state.loggedInUser = action.payload
        },
		logoutDeleteFromStorage:(state, action:PayloadAction)=>{
            state.loggedInUser = null
			localStorage.removeItem('user');
        }
	},
	//this section is for async thunk redux
	extraReducers:(builder)=>{
		//every asynchtyunk retyurns 3 state, the async function with thumnk
        //first state is fulfilled with is no error,  second state is loading state when async
        //funciton is not yet resolved, third one is error state, when async fncitn inside thunk returns error
		builder.addCase(doLogin.fulfilled,(state,action)=>{
            //action has the response payload
            state.loggedInUser = action.payload //storing the logged in user in the state
			localStorage.setItem('user', JSON.stringify(action.payload));
        })
		builder.addCase(doLogin.rejected, (state, action) => {
			state.loggedInUser = null;
			
		});
	}
})	

//this exports extra reducers automatically
export default LoginSlice.reducer;
//this exports regular reducers
export const { loadUserFromStorage,logoutDeleteFromStorage } = LoginSlice.actions
