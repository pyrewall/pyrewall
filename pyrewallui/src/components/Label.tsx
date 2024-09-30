import React, { DetailedHTMLProps, HTMLProps, LabelHTMLAttributes } from "react";

const Label: React.FC<DetailedHTMLProps<LabelHTMLAttributes<HTMLLabelElement>, HTMLLabelElement>> = ({className, ...otherProps}) => {
    return <label className={`block mb-2 text-sm font-medium text-gray-900 ${className}`} {...otherProps} />
}

export default Label;