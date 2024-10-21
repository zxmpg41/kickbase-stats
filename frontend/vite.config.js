import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  build: {
    outDir: './dist',
  },
  base: '/kickbase-stats',
  plugins: [react()],
  resolve: {
    alias: {
      '~': path.resolve(__dirname, './src'),
    },
  },
})
