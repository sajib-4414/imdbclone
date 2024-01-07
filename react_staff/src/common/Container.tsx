import React from "react";
import Header from "./Header";
import Footer from "./Footer";
import { ContainerProps } from "../interfaces/ContainerProps";

const Container: React.FC<ContainerProps> = ({ children }) => {
  return (
    <div>
      <Header />
      <div
        className="container"
        style={{ padding: "20px", marginBottom: "100px" }}
      >
        {children}
      </div>
      <Footer />
    </div>
  );
};
export default Container;
