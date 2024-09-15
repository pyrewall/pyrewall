import React from "react";
import { Outlet } from "react-router-dom";

const Layout: React.FC = () => {
    return (
        <div className="h-screen w-screen flex flex-row">
            <div className="w-1/5 h-screen bg-slate-800 shadow-lg shadow-slate-800 z-10">
                <div className="w-full bg-slate-950 text-white text-3xl font-bold text-center py-4">Pyrewall</div>
            </div>
            <div className="w-4/5 h-screen bg-slate-50">
                <Outlet />
            </div>
        </div>
    );
};

export default Layout;