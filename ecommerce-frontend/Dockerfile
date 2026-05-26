FROM nginx:alpine

# Copiar archivos estáticos del frontend
COPY . /usr/share/nginx/html

# Copiar configuración personalizada de nginx (proxy reverso)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
