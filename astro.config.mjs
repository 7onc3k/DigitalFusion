import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";
import node from "@astrojs/node";

import icon from "astro-icon";
export default defineConfig({
  integrations: [tailwind(), icon()],
  output: "server",
  adapter: node({ mode: 'standalone' })
});