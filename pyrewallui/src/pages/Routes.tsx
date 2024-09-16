import React from "react";
import { createBrowserRouter, Navigate, RouterProvider } from "react-router-dom";
import Layout from "../components/Layout";
import SystemGroupsPage from "./System/Groups";
import SystemUsersPage from "./System/Users";

const router = createBrowserRouter([
    {
        path: '/',
        element: <Layout />,
        children: [
            {
                index: true,
                element: <Navigate to={'/dashboard'} />
            },
            {
                path: 'dashboard',
                element: <></>
            },
            {
                path: 'system',
                children: [
                    {
                        path: 'groups',
                        element: <SystemGroupsPage />
                    },
                    {
                        path: 'users',
                        element: <SystemUsersPage />
                    }
                ]
            }
        ]
    }
]);

const AppRoutes: React.FC = () => {
    return <RouterProvider router={router} />;
};

export default AppRoutes;