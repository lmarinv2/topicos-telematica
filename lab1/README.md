# st0263-2266 Topicos especiales en telemática
## Estudiante: Laura Marin Velez - lmarinv2@eafit.edu.co
## Profesor: Edwin Nelson Montoya Múnera - emontoya@eafit.edu.co
# Laboratorio 1
## Descripcion 
Este laboratorio se trata sobre el protocolo HTTP mediante sockest, usando la arquitectura cliente servidor, especificamente se implementara el metodo GET que consite en traer informacion
## Instalacion 
Se debe iniciar una instacia en EC2 que será el servidor, deben de estar habilitados los puertos 80 y 22 que son lo sque escuchan http y https, adicionalmente el servidor debe tener asociada una direccion ip elastica. La instancia debe tener instalada python 3 y git 
```
sudo yum install git
sudo yum install python3
```
## Ejecucion
Inicializar la instancia servidor y clonar el repositorio, y se corre el archivo server.py
```
sudo python server.py
```
Luego vamos nuestro browser y ponemos la direccion elastica del servidor mas el nombre del archivo que necesitamos
```
IPelastica/archivo
```
## Fuentes
* Proyecto 2 Telematica
* https://github.com/Shiroke-013/TET_LABS/blob/b29a91ebc31742a55285cf6fb8bf536a5241b9bb/Lab2/Chat_Server.py
* https://www.youtube.com/watch?v=TTE-ZxN3XkA&ab_channel=AlejandroAlvarez
