#!/bin/sh

read -p "Si desea crear un contenedor de BD relacional como MariaDB seleccione Yes (Y/n): " rest1
if [ $rest1 = "y" ] || [ $rest1 = "Y" ] || [ $rest1 = "yes" ] || [ $rest1 = "YES" ] || [ $rest1 = "" ]; then
read -p "Ingrese el nombre de la imagen base que desea descargar: " imgBase
read -p "Ingrese nombre de contenedor: " name
read -p "Ingrese su variable de password root: " VarPassR   
read -p "Ingrese password del usuario ROOT: " passRoot
read -p "Ingrese su variable para nombre de BD: " VarNamBD
read -p "Ingrese nombre de Base de Datos: " nameBD
read -p "Ingrese su variable para nombre de usuario BD: " VarNamUserBd
read -p "Ingrese nombre del usuario de Base de Datos: " nameUser
read -p "Ingrese su variable para password de usuario BD: " VarNamPassBd
read -p "Ingrese Password del usuario de la Base de Datos: " passUser
read -p "Ingrese número del puerto: " nunPort

docker run -d --name $name -p $nunPort -e $VarPassR=$passRoot -e $VarNamBD=$nameBD -e $VarNamUserBd=$nameUser -e $VarNamPassBd=$passUser $imgBase
fi


#""" docker run --name bbdd, 
#--env MARIADB_ROOT_PASSWORD=root 
#--env MARIADB_DATABASE=prueba 
#--env MARIADB_USER=invitado
#--env MARIADB_PASSWORD=invitado
# mariadb --port 3306 """