import React,{ReactNode } from "react";
import Header from "./Header";
import Footer from "./Footer";

interface ContainerProps {
    children: ReactNode;
}

const Container:React.FC<ContainerProps> =({children})=>{
    return(
        <div>
            <Header/>
            <div className="container" style={{ padding: '20px', marginBottom: '100px' }}>
                {children}
            </div>
            <Footer/>
        </div>
    )
}
export default Container;