##Script para Ejecutar un contenedor en segundo plano, en el caso de no tener la imagen tambien la descarga automatico.
#Para poder correr este script hay q instalar el SDK con --- pip install docker

import docker
client = docker.from_env()
container = client.containers.run((input("\nNombre de la imagen que desea descargar (ejemplo nginx:alpine):  ")),
ports={(input("Puerto Docker+protocolo (ejemplo 80/tcp):  ")): (input("Puerto Host:  "))}, 
name=(input("Nombre del servidor web:  ")), detach=True)

for image in client.images.list():
    print("-------------------------------------------\n")
    print("El hash de su imagen descargada previamente es: "+str(image.short_id))
    print("Esta imagen se llama: "+str(image.tags))
    print("Esta imagen corresponde a: "+str(image.labels))

for containers in client.containers.list():   
    print("\n Container creado: "+str(containers.short_id)) 
    print("   Nombre Container: "+str(containers.name))
    print("   Puertos: "+str(containers.ports))
    print("   Etiquetas: "+str(containers.labels))
    
