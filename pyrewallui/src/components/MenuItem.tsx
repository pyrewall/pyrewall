import React from "react";
import { Link, NavLink } from "react-router-dom";

interface MenuItemProps {
    to: string;
    children?: React.ReactNode;
}

const MenuItem: React.FC<MenuItemProps> = (props) => {
    return <div className="px-2 py-1 hover:bg-slate-700">
        <NavLink to={props.to} className={(props) => (
            props.isActive ? "font-bold underline" : ""
        )}>
            {props.children}
        </NavLink>
    </div>
};

export default MenuItem;