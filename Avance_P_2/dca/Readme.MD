## Informacion de la materia:

- ST0263 TOPICOS EN TELEMATICA

## Estudiante(s):

- Andres Danilo Patiño Velez, apatin14@eafit.edu.co
- Laura Marin Gomez, lmarinv2@eafit.edu.co

## Profesor:

- Edwin Nelson Montoya Munera

## Actividad:

- Avance proyecto 2

## 1. breve descripción de la actividad

Desplegar una aplicación open source LAMP de comunidad que represente un sistema de
información del tipo Sistema de Gestión de Aprendizaje (LMS, por sus siglas en inglés). En
este caso se seleccionará Moodle

### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

- Desplegar en entornos separados cada uno de los elementos necesarios para implementar un LMS (Moodle) en el ambiente de AWS
- Desplegar en entornos separados cada uno de los elementos necesarios para implementar un LMS (Moodle) en el ambiente del DCA
- Conectar las aplicaciones haciendo uso de redes internas
- Alta Disponibilidad:
  - Balanceadores de carga
  - Crecimiento horizontal
  - Disponibilidad en la capa de servicios 
  - Disponibilidad en la capa de persistencia de datos para el manejo de
archivos.
  - Disponibilidad en la capa de bases de datos para el manejo de la información
almacenada en el motor definido para esto.
  - Sistema de backup y restore de datos, contenidos, aplicaciones, etc

## 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

Se despliega utilizando la estrategias de contenedores aislados sincronizados por la configuracion del 

## Informacion de los desplieuges por Componentes.

### Proveedor 1 (Base de datos)

  - Actualizamos la instancia de ubuntu

``` ssh
Sudo apt update
```
  - instalamos docker y docker-compose 

``` ssh
sudo apt install docker.io -y
sudo apt install docker-compose -y
```
  - habilitamos el proceso

``` ssh
sudo systemctl enable Docker
sudo systemctl start Docker
```
  - entregamos permisos al usuario

``` ssh
sudo usermod -a -G docker Ubuntu
```
  - generamos la carpeta **mariadb** donde vamos a depositar la configuracion de la instancia del contenedor

``` ssh
sudo mkdir mariadb
cd mariadb
sudo nano docker-compose.yml
```

  - ejecutamos la instancia del contenedor desde docker-compose

``` ssh
docker-compose up --build -d
```

### Proveedor 2 (NFS-Server)


  - Actualizamos la instancia de ubuntu

``` ssh
Sudo apt update
```
  - instalamos el servidor NFS

``` ssh
sudo apt install nfs-kernel-server
```
  - configuramos la carpeta donde se van a subir los archivos compartidos

``` ssh
sudo mkdir -p /mnt/nfs_share
sudo chown -R nobody:nogroup /mnt/nfs_share/
sudo chmod 777 /mnt/nfs_share/
sudo nano /etc/exports
sudo exportfs -a
```

  - Reinciamos el proceso

``` ssh
sudo systemctl restart nfs-kernel-server
```
  - Configuramos el firewall para las solicitudes al puerto del nfs

``` ssh
sudo ufw allow from 192.168.0.0/16 to any port nfs
sudo ufw enable
```
### Cliente NFS

  - Actualizamos la instancia de ubuntu

``` ssh
Sudo apt update
```

  - Instalamos el cliente de NFS (nfs-common)

``` ssh
sudo apt install nfs-common
```

  - Montamos el volumen donde se van a almacenar y recuperar los archivos del nfs

``` ssh
sudo mkdir -p /mnt/Moodle
sudo mount 192.168.19.141:/mnt/nfs_share /mnt/Moodle
```
> 192.168.19.141 corresponde a la direccion ip privada el nfs

>Pruebas de cargas
>
>En server: 
> - cd /mnt/nfs_share/
> -touch sample1.text sample2.text
>
>En cliente:
> - ls -l /mnt/Moodle
> 


### Moodle (Servicio 1 - Servicio 2)

  - Actualizamos la instancia de ubuntu

``` ssh
Sudo apt update
```
  - instalamos docker y docker-compose 

``` ssh
sudo apt install docker.io -y
sudo apt install docker-compose -y
```
  - habilitamos el proceso

``` ssh
sudo systemctl enable Docker
sudo systemctl start Docker
```
  - entregamos permisos al usuario

``` ssh
sudo usermod -a -G docker Ubuntu
```

- generamos la carpeta **Moodle** donde vamos a depositar la configuracion de la instancia del contenedor

``` ssh
Sudo mkdir Moodle
Cd Moodle
Sudo nano Docker-compose.yml
```
- ejecutamos la instancia del contenedor desde docker-compose

``` ssh
docker-compose up --build -d
```

### Balanceador de cargas (Servicio 1 - Servicio 2)

  - Actualizamos la instancia de ubuntu

``` ssh
Sudo apt update
```
  - instalamos letsencrypt y nginx

``` ssh
sudo add-apt-repository ppa:certbot/certbot
sudo apt install letsencrypt -y
sudo apt install nginx -y
```
  - Creo la carpeta para depositar los certificados

``` ssh
sudo mkdir -p /var/www/letsencrypt
```
  - Reiniciamos el proceso de Nginx

``` ssh
sudo service nginx reload
```

  - Generamos los certificados

``` ssh
sudo certbot --server https://acme-v02.api.letsencrypt.org/directory -d *.equipo4.tk --manual --preferred-challenges dns-01
certonly
```

- generamos la carpeta **nginx** donde vamos a depositar la configuracion de la instancia del contenedor y pegamos los certificados

``` ssh
sudo mkdir nginx
cd nginx/
sudo mkdir ssl
cp /etc/letsencrypt/live/equipo4.tk/* /home/ubuntu/nginx/ssl/
```
- Modificamos la configuracion de nginx

``` ssh
sudo nano /etc/nginx/nginx.conf
```

- Validamos que las configuraciones sean correctas y reinicamos el servicio

``` ssh
sudo nginx -t 
sudo service reload
```

- Creamos el archivo sudo nano **options-ssl-nginx.conf** y lo copiamos dentro de la carpeta del proyecto

> Si su computador cuenta con el archivo options-ssl-nginx.config omita este paso

``` ssh
sudo nano /etc/letsencrypt/options-ssl-nginx.conf
sudo cp /etc/letsencrypt/options-ssl-nginx.conf /home/ubuntu/nginx/ssl/
```
- Generamos el archivo ssl-dhparams.pem dentro de la carpeta ssl del proyecto

``` ssh
cd nginx/ssl
sudo openssl dhparam -out ssl-dhparams.pem 512
```

- Creamos el archivo **docker-compose.yml** con al configuracion del docker en la raiz del proyecto

``` ssh
cd nginx
sudo nano docker-compose.yml
```

- Cambiamos la configuracion del nginx del proyecto

``` ssh
sudo nano nginx.conf
```

-desplegamos el docker compose

``` ssh
docker-compose up --build -d
```

### detalles del desarrollo.

El desarrollo esta generado en python con una arquitectura Cliente/Servidor, en la cual se encuentra en la raiz el archivo correspondiente a las variables de entorno `.env` la cual contiene la configuracion de la aplicacion.

### opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)

- 📁./
-  |
  - ├─📁maria db
    - ├───| docker-compose.yaml
  - ├─📁Moodle
    - ├───| docker-compose.yaml
  - ├─📁Nginx
    - ├───📁 ssl
      - ├───| nginx.config
      - ├───| options-ssl-nginx.conf
      - ├───| ssl-dhparams.pem
    - ├───| docker-compose.yml


## 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

- Virtual Machines
  - Moodle 1
  - Moodle 2
  - NFS
  - Base de datos
  - Balanceador de cargas
- Paquetes
  - docker
  - docker-compose
  - nfs-kernel-server
  - letsencrypt 
  - nginx
  - openssl 

## IP o nombres de dominio en nube o en la máquina servidor.


#### versión README.md -> 1.0 (2022-noviembre)
