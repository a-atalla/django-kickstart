import { defineConfig } from 'vite'
import djangoVite from 'django-vite-plugin'

export default defineConfig({
    plugins: [
        djangoVite([
            'theme/js/main.js',
            'theme/css/main.css',
        ])
    ],
});