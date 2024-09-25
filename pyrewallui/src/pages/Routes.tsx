import React from "react";
import { createBrowserRouter, Navigate, RouterProvider } from "react-router-dom";
import Layout from "../components/Layout";
import SystemGroupsPage from "./System/Groups";
import SystemUsersPage from "./System/Users";
import SystemCreateUserPage from "./System/Users/Create";

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
                        element: <SystemUsersPage />,
                        children: [
                            {
                                'path': 'new',
                                element: <SystemCreateUserPage />
                            }
                        ]
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