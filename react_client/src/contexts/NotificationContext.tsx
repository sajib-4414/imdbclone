import React, {createContext, ReactNode, useContext, useState, useEffect} from 'react'
import { toast, ToastContainer, ToastOptions } from 'react-toastify';

export enum ToastType {
    Info = 'info',
    Success = 'success',
    Error = 'error',
}

type ToastConfig = {
    type: ToastType;
    length?:number;
}
export interface NotificationContextProps{
    showNotification:(message:string, config?: ToastConfig) => void;
}

const NotificationContext = createContext<NotificationContextProps|undefined>(undefined);

export const NotificationProvider:React.FC<{children:ReactNode}> = ({children}) =>{
    const [message, setMessage] = useState<string|null>(null);
    const resetMessage = ()=>{
        setMessage(null)
    }
    const showNotification = (message:string, config?: ToastConfig) =>{
        const toastOptions:ToastOptions = {
            autoClose: config?.length || 3000,
        }
        let toastFunction:(message:string, options?: ToastOptions) => void = toast;
            switch(config?.type){
                case ToastType.Error:
                    toastFunction = toast.error
                    break
                case ToastType.Success:
                    toastFunction = toast.success
                    break;
                case ToastType.Info:
                    toastFunction = toast.info
                    break;
            }
        toastFunction(message, toastOptions)
    }
    useEffect(()=>{
        //everytime message is changed, reset the message in 3s
        const timeoutId = setTimeout(() => {
            resetMessage();
          }, 3000);
        return () => clearTimeout(timeoutId);

    },[message])

    return (
        <NotificationContext.Provider value={{ showNotification}}>
            <ToastContainer/>
            {children}
        </NotificationContext.Provider>
    )
}

export const useNotification = ()=>{
    const context = useContext(NotificationContext);
    if (!context) {
        throw new Error('useNotification must be used within a NotificationProvider');
    }
    return context;
}