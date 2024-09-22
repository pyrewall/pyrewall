import React, { createContext, useContext, useEffect, useState } from "react";
import LoginPage from "../pages/Login";
import useSessionStorageBackedState from "../libs/useSessionStorageBackedState";
import { AuthenticatedUser } from "../api";

export interface UserContextData {
    user: AuthenticatedUser;
    logout: () => void;
};

const UserContext = createContext<UserContextData | null>(null);

UserContext.displayName = 'UserContext';

interface UserContextProviderProps {
    children: React.ReactNode;
}

export const UserContextProvider: React.FC<UserContextProviderProps> = (props) => {
    const [user, setUser] = useSessionStorageBackedState<AuthenticatedUser | undefined>('pyrewall-user', undefined);

    const logout = () => {
        setUser(undefined);
    }

    useEffect(() => {
        if (user == null) return;

        const expires = new Date(user.token.expires_at).getTime()
        const diff = expires - (new Date().getTime());

        console.log("Session expires in ", diff)

        const timeout = setTimeout(() => {
            logout()
        }, diff);

        return () => {
            clearTimeout(timeout);
        }
    }, [user])

    if (user == null) {
        return <LoginPage setUser={setUser} />
    }

    const data: UserContextData = {
        user,
        logout
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