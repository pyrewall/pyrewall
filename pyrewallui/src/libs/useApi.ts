import { Zodios } from "@zodios/core"
import { AuthenticationEndpoints } from "../api"

export const useAuthenticationApi = () => {
    return new Zodios(import.meta.env.VITE_API_URL, AuthenticationEndpoints);
}