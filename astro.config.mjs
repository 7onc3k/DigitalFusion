import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";
import icon from "astro-icon";
import react from '@astrojs/react';

export default defineConfig({
  integrations: [tailwind(), icon(), react()]
});