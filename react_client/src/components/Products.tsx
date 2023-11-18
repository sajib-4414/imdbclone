import React from "react";
import { products } from "../dummyData";
import { addToCart } from "../store/features/cartSlice";
import { useAppDispatch } from "../store/store";

export const Products = () => {
  const dispatch = useAppDispatch();
  return (
    <div>
      {products.map((product) => (
        <div key={product.id}>
          <img src="https://img.freepik.com/free-photo/painting-mountain-lake-with-mountain-background_188544-9126.jpg" />
          <p>{product.name}</p>
          <p>{product.id}</p>
          <button onClick={() => dispatch(addToCart({ product, qty: 1 }))}>
            Add to Cart
          </button>
        </div>
      ))}
    </div>
  );
};
