import path from "path"
import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"
import { ghPages } from "vite-plugin-gh-pages";

export default defineConfig(({ command }) => {
  return {
    base: command === 'build' ? '/renai-tool/' : '/',
    plugins: [react(), ghPages()],
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "./src"),
      },
    },
    server: {
      port: 3005,
    },
  }
})
