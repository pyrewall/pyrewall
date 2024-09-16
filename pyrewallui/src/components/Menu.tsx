import React, { useState } from "react";

interface MenuProps {
    display: React.ReactNode;
    children?: React.ReactNode;
}

const Menu: React.FC<MenuProps> = (props) => {
    const [expanded, setExpanded] = useState(false);

    const toggleExpanded = () => {
        setExpanded(!expanded);
    }

    return <>
        <div className="w-full flex cursor-pointer bg-slate-900 border-b border-slate-700" onClick={toggleExpanded}>
            <div className="my-auto p-2 text-lg">{props.display}</div>
            <div className="ml-auto p-2 text-lg">
                {expanded ? <><i className="bi bi-caret-down-fill"></i></> : <><i className="bi bi-caret-up-fill"></i></>}
            </div>
        </div>
        {expanded && <div className="w-full">
            {props.children}
        </div>}
    </>;
}

export default Menu;