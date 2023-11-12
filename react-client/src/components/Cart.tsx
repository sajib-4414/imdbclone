import React from 'react';
import { useAppSelector } from '../store/store';
import { CartItem, totalItemQtySelector, totalQtyLimitSelector } from '../store/features/cartSlice';
export const Cart = () => {
  const isExceeded = useAppSelector((state)=> totalQtyLimitSelector(state,5))
    const totalItemQty = useAppSelector(totalItemQtySelector)
    return (
      <div>
        <div>
          <span>Cart items count:</span><span>{totalItemQty}</span>
        </div>
        <div>
          <span>Is exceeded</span><span>{isExceeded?"Yes":"No"}</span>
        </div>
      </div>
    );
  };
  