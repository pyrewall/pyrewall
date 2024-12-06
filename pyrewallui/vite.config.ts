import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import fs from 'fs';

const version = fs.readFileSync('../VERSION')

process.env['VITE_PYREWALL_VERSION'] = version.toString()

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
})
