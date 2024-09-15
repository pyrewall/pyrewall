import React from "react";
import { Outlet } from "react-router-dom";
import { useUserContext } from "../contexts/UserContext";

const Layout: React.FC = () => {
    const userContext = useUserContext();

    return (
        <div className="h-screen w-screen flex flex-row">
            <div className="w-1/5 h-screen bg-slate-800 shadow-lg shadow-slate-800 z-10">
                <div className="w-full h-16 bg-slate-950 text-white text-3xl font-bold flex py-4">
                    <div className="m-auto">Pyrewall</div>
                </div>
                <div className="w-full h-[calc(100vh-64px)] overflow-y-scroll">

                </div>
            </div>
            <div className="w-4/5 h-screen bg-slate-50">
                <div className="w-full h-16 bg-slate-900 text-white shadow-lg shadow-slate-900 flex">
                    <div>

                    </div>
                    <div className="ml-auto flex">
                        <div className="text-xl my-auto">
                            {userContext.user.user.full_name ?? userContext.user.user.username}
                        </div>
                        <div className="my-auto">
                            <button onClick={userContext.logout} title="Logout" className="cursor-pointer">
                                <i className="bi bi-box-arrow-left text-4xl p-2 mr-4"></i>
                            </button>
                        </div>
                    </div>
                </div>
                <Outlet />
            </div>
        </div>
    );
};

export default Layout;