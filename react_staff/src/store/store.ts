import { configureStore } from "@reduxjs/toolkit";
import { useDispatch, useSelector, TypedUseSelectorHook } from "react-redux";
import { LoginSlice } from "./features/loginSlice";
// import {TypedUseSelectorHook} from "react-redux/es/types"
export const store = configureStore({
  reducer: {
    loginUser: LoginSlice.reducer,
  },
});

//these 2 lines are for typescript
export type RootState = ReturnType<typeof store.getState>;
export const useAppDispatch: () => typeof store.dispatch = useDispatch;
export const useAppSelector: TypedUseSelectorHook<
  ReturnType<typeof store.getState>
> = useSelector;
