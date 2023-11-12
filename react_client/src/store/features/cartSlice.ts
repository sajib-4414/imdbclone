import { createSelector, createSlice, PayloadAction } from "@reduxjs/toolkit";
import { RootState } from "../store";

export interface Product{
    id:number;
    name:string;
    price:number;
}

export interface CartItem{
    product:Product;
    qty: number;
}

interface CartState{
    items:CartItem[];
}

const initialState:CartState = {
    items: []
}

export const CartSlice = createSlice({
    name:"cart",
    initialState,
    reducers:{
        //this is cartslice action
        addToCart:(state, action:PayloadAction<CartItem>)=>{
            state.items.push(action.payload)
        }
    }
})

export default CartSlice.reducer;
export const {addToCart} = CartSlice.actions;

const items = (state:RootState)=> state.cart.items
//in this way we can memoize our selector and optimize redux store functionality.
export const totalItemQtySelector = createSelector([items],(items)=>
{
    console.log("custom selector ran")
    return items.reduce((total:number,curr:CartItem)=>(total+= curr.qty),0)
}
,)

//custom seelctor with 2 input seelect, one is item, anotehr is function,
//that takes all the previouis input seelctor+paramter passed which is limit here
//callback funciton retuns a limit
//limit can be accessed in the third selector as we are returning it from the method (items, limit:number)=>limit
export const totalQtyLimitSelector = createSelector([items,(items, limit:number)=>limit],(items,limit)=>{
    const total = items.reduce(
        (total:number, curr:CartItem)=>(total +=curr.qty),0
    )
    return total>limit
})