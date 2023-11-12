import { createAsyncThunk, createSlice, PayloadAction } from "@reduxjs/toolkit";


export interface Person{
    id: number;
    name: string;
}

interface PersonState{
    persons:Person[]
}

const initialState:PersonState = {
    persons: [],
}

//unique key, async funciton
export const fetchPerson = createAsyncThunk("person/fetch",async (thunkAPI)=>{
    const response = await fetch("http://localhost:3002/person", {
        method: "GET"
    })
    const data = response.json();
    return data
})

//unique key, async funciton
export const savePerson = createAsyncThunk("person/save",async (name:string, thunkAPI)=>{
    const response = await fetch("http://localhost:3002/person", {
        method: "POST",
        headers:{
            "Content-Type": "application/json"
        },
        body:JSON.stringify({
            name
        })
    })
    const data = await response.json();//data will have name and id inside it
    return data;
})

export const PersonSlice = createSlice({
    name: "person",
    initialState,
    reducers:{
        addPerson:(state, action:PayloadAction<{name: string}>)=>{
            state.persons.push({
                id: state.persons.length,
                name: action.payload.name
            })
        }
    },
    extraReducers:(builder)=>{
        //every asynchtyunk retyurns 3 state, the async function with thumnk
        //first state is fulfilled with is no error,  second state is loading state when async
        //funciton is not yet resolved, third one is error state, when async fncitn inside thunk returns error
        builder.addCase(fetchPerson.fulfilled,(state,action)=>{
            //action has the response payload
            state.persons = action.payload
        })
        
        builder.addCase(savePerson.fulfilled, (state, action)=>{
            state.persons.push(action.payload)
        })
    }
})

export default PersonSlice.reducer;
export const { addPerson } = PersonSlice.actions