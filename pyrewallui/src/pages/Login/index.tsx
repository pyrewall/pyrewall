import React, { FormEvent, useState } from "react";
import loginBackground from '../../assets/backgrounds/cincinnati-bridge.jpg';
import AuthenticatedUser, { AuthenticatedUserSchema } from "../../types/AuthenticatedUser";

interface LoginPageProps {
    setUser: (user: AuthenticatedUser) => void;
}

const LoginPage: React.FC<LoginPageProps> = (props) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const doLogin = (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        void (async () => {
            const loginData = {
                username,
                password
            };

            const response = await fetch(`${import.meta.env.VITE_API_URL}api/v1/auth/login`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(loginData)
            });

            const data = await AuthenticatedUserSchema.parseAsync(await response.json());

            props.setUser(data);
        })();
    };

    return <>
        <div className="w-full h-full" style={{
            backgroundImage: `url(${loginBackground})`,
            backgroundSize: 'cover'
        }}>
            <div className="w-full h-full md:h-[75vh] flex">
            <div className="my-auto mx-auto md:ml-auto md:mr-96">
                <h2 className="text-4xl text-center text-white p-4 drop-shadow-lg"><span className="font-bold">Pyrewall</span> | <span className="font-normal">Login</span></h2>
                <form onSubmit={doLogin}>
                    <div>
                        <input placeholder="Username" className="w-72 rounded px-2 py-1 selection:border-blue-600" value={username} onChange={(e) => setUsername(e.target.value)} />
                    </div>
                    <div className="my-2">
                        <input type="password" placeholder="Password" className="w-72 rounded px-2 py-1 selection:border-blue-600" value={password} onChange={(e) => setPassword(e.target.value)} />
                    </div>
                    <div>
                        <button type="submit" className="w-72 rounded px-2 py-1 text-white bg-slate-950 hover:bg-slate-800">Login</button>
                    </div>
                </form>
            </div>
        </div>
        <div style={{right: 0, bottom: 0}} className="absolute p-1 text-center text-white text-sm">
            v{'test'}
        </div>
        </div>
    </>;
};

export default LoginPage;