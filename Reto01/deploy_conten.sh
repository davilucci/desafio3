##Script para Ejecutar un contenedor en segundo plano, en el caso de no tener la imagen, tambien la descarga automatico

docker run -d --name servidor_web -p 8181:80 nginx:alpine

docker ps

docker images

