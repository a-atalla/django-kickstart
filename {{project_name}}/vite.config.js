import { defineConfig } from 'vite'
import djangoVite from 'django-vite-plugin'

export default defineConfig({
    plugins: [
        djangoVite([
            'theme/js/apj.js',
            'theme/css/styles.css',
        ])
    ],
});