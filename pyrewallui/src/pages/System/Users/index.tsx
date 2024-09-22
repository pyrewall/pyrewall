import React from "react";
import { useUserApi } from "../../../api";
import { useQuery } from "@tanstack/react-query";

const SystemUsersPage: React.FC = () => {
    const usersApi = useUserApi();

    

    const userData = useQuery({ queryKey: ['users'], queryFn: async () => {
        console.log("Fetching users list")
        const users = await usersApi.get_users_list()
        console.log(users);
        return users;
    }
    })

    return <>
        <div className="p-4">
            <h1 className="text-3xl">Users</h1>
            <div>
                {userData.data?.map((user) => (
                    <div key={user.id}>{user.username}</div>
                ))}
            </div>
        </div>
    </>;
};

export default SystemUsersPage;