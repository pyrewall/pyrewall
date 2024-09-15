import React, { createContext, useContext, useState } from "react";
import AuthenticatedUser from "../types/AuthenticatedUser";
import LoginPage from "../pages/Login";
import useSessionStorageBackedState from "../libs/useSessionStorageBackedState";

export interface UserContextData {
    user: AuthenticatedUser;
};

const UserContext = createContext<UserContextData | null>(null);

UserContext.displayName = 'UserContext';

interface UserContextProviderProps {
    children: React.ReactNode;
}

export const UserContextProvider: React.FC<UserContextProviderProps> = (props) => {
    const [user, setUser] = useSessionStorageBackedState<AuthenticatedUser | undefined>('pyrewall-user', undefined);

    if (user == null) {
        return <LoginPage setUser={setUser} />
    }

    const data: UserContextData = {
        user
    };

    return <UserContext.Provider value={data}>
        {props.children}
    </UserContext.Provider>
}

export const useUserContext = (): UserContextData => {
    const context = useContext(UserContext);

    if (context == null) {
        throw Error('Must be used within UserContextProvider');
    }

    return context;
}