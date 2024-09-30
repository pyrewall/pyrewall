import React, { DetailedHTMLProps, HTMLProps, InputHTMLAttributes } from "react";


const Input: React.FC<DetailedHTMLProps<InputHTMLAttributes<HTMLInputElement>, HTMLInputElement>> = ({className, ...otherProps}) => {
    return <input className={` bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5${className}`} {...otherProps} />
}

export default Input;