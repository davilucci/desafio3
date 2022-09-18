##Script para Ejecutar un contenedor en segundo plano, en el caso de no tener la imagen tambien la descarga automatico.
#Para poder correr este script hay q instalar el SDK con --- pip install docker

#Para crear varios contenedores, podemos clonar las lineas 11 hasta la 14, y agregamos los valores necesarios, así como retirar el modo iteractivo INPUT
#Cabe destacar que dicho script solo aplica para imagenes q usen variables de entorno.

import os
import docker
client = docker.from_env()

container = client.containers.run((input("\nNombre de la imagen que desea descargar (ejemplo nginx:alpine):  ")),
ports={(input("Puerto Docker + protocolo (ejemplo 80/tcp):  ")): (input("Puerto Host:  "))},
name=(input("Nombre del servidor web:  ")), detach=True, 
environment=["MARIADB_ROOT_PASSWORD=root", "MARIADB_DATABASE=prueba", "MARIADB_USER=invitado", "MARIADB_PASSWORD=invitado"])


"""docker run --name bbdd, 
--env MARIADB_ROOT_PASSWORD=root 
--env MARIADB_DATABASE=prueba 
--env MARIADB_USER=invitado
--env MARIADB_PASSWORD=invitado
mariadb --port 3306"""


for image in client.images.list():
    print("-------------------------------------------\n")
    print("El hash de su imagen descargada previamente es: "+str(image.short_id))
    print("Esta imagen se llama: "+str(image.tags))
    print("Esta imagen corresponde a: "+str(image.labels))

for containers in client.containers.list():   
    print("\n Container creado en este momento: "+str(containers.short_id)) 
    print("   Nombre Container: "+str(containers.name))
    print("   Puertos: "+str(containers.ports))
    print("   Etiquetas: "+str(containers.labels))
    print("   Este container corresponde a: "+str(containers.labels))
