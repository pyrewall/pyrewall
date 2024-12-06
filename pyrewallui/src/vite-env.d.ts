/// <reference types="vite/client" />

interface ImportMetaEnv {
    readonly VITE_API_URL: string;
    readonly VITE_PYREWALL_VERSION: string;
}

interface InterfaceMeta {
    readonly env: ImportMetaEnv;
}