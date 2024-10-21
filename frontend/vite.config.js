import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  build: {
    outDir: './build',
  },
  base: '/kickbase-analysis',
  plugins: [react()],
  resolve: {
    alias: {
      '~': path.resolve(__dirname, './src'),
    },
  },
})
