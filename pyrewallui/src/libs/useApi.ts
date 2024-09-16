import { ApiClient, createApiClient } from "../api";
import { useUserContext } from "../contexts/UserContext";

export const useApi = (): ApiClient => {
    const { user: { token: { access_token } } } = useUserContext();
    const api = createApiClient((method, url, parameters) => (
        fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${access_token}`
            },
            body: JSON.stringify(parameters)
        })
    ), import.meta.env.VITE_API_URL);

    return api;
}

export const useUnauthenticatedApi = (): ApiClient => {
    const api = createApiClient((method, url, parameters) => (
        fetch(url, {
            method: method,
            headers: {
                ...parameters?.header,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(parameters?.body)
        }).then(r => r.json())
    ), import.meta.env.VITE_API_URL);

    return api;
}