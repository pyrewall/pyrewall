import React from "react";
import { createBrowserRouter, Navigate, RouterProvider } from "react-router-dom";
import Layout from "../components/Layout";

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
            }
        ]
    }
]);

const AppRoutes: React.FC = () => {
    return <RouterProvider router={router} />;
};

export default AppRoutes;