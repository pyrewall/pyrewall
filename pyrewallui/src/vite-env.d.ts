/// <reference types="vite/client" />

interface ImportMetaEnv {
    readonly VITE_API_URL: string;
}

interface InterfaceMeta {
    readonly env: ImportMetaEnv;
}