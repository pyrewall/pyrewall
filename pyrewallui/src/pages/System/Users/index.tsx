import React from "react";
import { User, useUserApi } from "../../../api";
import { useQuery } from "@tanstack/react-query";
import { createColumnHelper, flexRender, getCoreRowModel, useReactTable } from "@tanstack/react-table";
import { Outlet } from "react-router-dom";

const columnHelper = createColumnHelper<User>();

const columns = [
    columnHelper.accessor('username', {
        header: 'Username',
        cell: info => info.getValue()
    }),
    columnHelper.accessor('full_name', {
        header: 'Full Name',
        cell: info => info.getValue()
    }),
    columnHelper.accessor('enabled', {
        header: 'Enabled?',
        cell: info => info.getValue() ? 'Enabled' : 'Disabled'
    })
];

const SystemUsersPage: React.FC = () => {
    const usersApi = useUserApi();

    const userData = useQuery({ queryKey: ['users'], queryFn: async () => {
        console.log("Fetching users list")
        const users = await usersApi.get_users_list()
        console.log(users);
        return users;
    }
    })

    const table = useReactTable({
        columns,
        data: userData.data ?? [],
        getCoreRowModel: getCoreRowModel()
    })

    return <>
        <div className="p-4">
            <h1 className="text-3xl">Users</h1>
            <div>
                <table className="table table-auto w-full">
                    <thead>
                        {table.getHeaderGroups().map((headerGroup) => (
                            <tr key={headerGroup.id}>
                                {headerGroup.headers.map((header) => (
                                    <th key={header.id} colSpan={header.colSpan}>{flexRender(header.column.columnDef.header, header.getContext())}</th>
                                ))}
                            </tr>
                        ))}
                    </thead>
                    <tbody>
                        {table.getRowModel().rows.map((row) => (
                            <tr key={row.id}>
                                {row.getVisibleCells().map((cell) => (
                                    <td key={cell.id}>{flexRender(cell.column.columnDef.cell, cell.getContext())}</td>
                                ))}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
        <Outlet />
    </>;
};

export default SystemUsersPage;