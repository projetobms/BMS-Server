# Dockerfile

FROM nginx:latest

# Copiar a configuração do Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copiar os certificados SSL
COPY certs/ /etc/letsencrypt/live/labnvh.online/

# Expor as portas 80 e 443
EXPOSE 80
EXPOSE 443

# Comando para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"]
