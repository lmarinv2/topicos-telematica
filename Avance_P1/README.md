# st0263-2266 Topicos especiales en telemática
## Estudiante: Laura Marin Velez - lmarinv2@eafit.edu.co
## Profesor: Edwin Nelson Montoya Múnera - emontoya@eafit.edu.co
#
# Avance proyecto 1
#
# 1. breve descripción de la actividad
El avance del proyecto consiste en instalar y configurar la base de datos de redis


## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

* Instalacion y configuracion de redis local y modo cluster desplegado en AWS 
* Configuracion de persistencia en disco 
* Servidor conctado mediante la linea de comando redis-cli
* Consultas CRUD desde python
* Implementacion de redis mediante las caracteristicas de MOM


## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

* Desarrollo de redis en modo cluster mediante diferentes instacias  

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

El nombre Redis proviene de las iniciales de Remote Dictionary Server (servidor de diccionario remoto), un tipo de servidor apto como memoria rápida para datos. Como sistema de gestión de base de datos (SGBD), Redis ofrece tanto una base de datos en memoria (in-memory database) como de clave-valor (key-value store)

La arquitectura de Redis es de tipo cliente-servidor. El cliente y el servidor pueden encontrarse en el mismo nodo o bien estar distribuidos. El servidor se encarga de almacenar datos en memoria.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## 1. Como se compila y ejecuta.
* lanzar la instacia y ejecutar 

    ``` 
    $ redis-cli
    ```

* Autenticar usuario 

    ``` 
    $ AUTH password
    ```

* Realizar CRUD con python 

    ``` 
    $ python3 nombre_archivo.py
    ```
    Archivos disponibles:


* Acceder a modo cluster
    Primero accedemos a la carperta

    Puertos 7000 7001 7002 7003 7004 7005

    ```
   $ ~/cluster-test/PORT 
    ``` 
    Y ejecutamos 

    ```
    $ redis-server ./redis.conf
    ```
    hacemos esto para cada puerto, cada uno en una terminal diferente 

    Ahora escogemos un nodo al azar y lo ejecutamos como cliente en otra terminal(PORT debe ser igual al nombre de la carpeta)

    ``` 
    $ redis-cli -c -p PORT
    ```

    Puertos disponibles:
   - 7000
    - 7001
    - 7002
    - 7003
    - 7004
    - 7005

    Por ultimo podemos hacer operacion CRUD desde redis-cli y python 


## 2. detalles del desarrollo.


## 3. detalles técnicos
Se lanzo una instacia de ubuntu 22.04
Se utilizo redis version y python version hiredis lsb-release
## 4. descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

Al instalar Redis este descarga un archivo redis.conf.

```
cd /ect/redis/redis.conf
```
- PUERTO Y HOST por el cual se comunican

    bind 127.0.0.1
    6379

- CONTRASEÑA

    required password

- HABILITAR MODO CLUSTER

    cluster-enabled 
    cluster-config-file 
    cluster-node-timeout
    cluster-slave-validity-factor
    cluster-migration-barrier
    cluster-require-full-coverage
    cluster-allow-reads-when-down


# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

# IP o nombres de dominio en nube o en la máquina servidor.


## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

## como se lanza el servidor.
```
redis-cli
```

![image](https://user-images.githubusercontent.com/53051440/187494575-83f342fc-e784-45b2-b761-a2980b2781fe.png)

![image](https://user-images.githubusercontent.com/53051440/187495052-1b7121ef-dfc5-450b-b696-243b12f4c59e.png)

![image](https://user-images.githubusercontent.com/53051440/187495084-d26f308d-4a0f-4cbb-a849-9f0671146fd9.png)

* CRUD desde redis-cli
![image](https://user-images.githubusercontent.com/53051440/187495168-c27e8d39-0a57-47b0-8734-b9f64f869a44.png)
![image](https://user-images.githubusercontent.com/53051440/187495197-fb7c4be1-e07e-40f4-9edc-371f09d0ae44.png)
![image](https://user-images.githubusercontent.com/53051440/187495232-23ed51d0-50de-4fff-8c80-56cef71ae960.png)
![image](https://user-images.githubusercontent.com/53051440/187495269-1bfbfa56-0c93-4639-8cef-b1b7f133ced3.png)




## una mini guia de como un usuario utilizaría el software o la aplicación

## opcionalmente - si quiere mostrar resultados o pantallazos 

# 5. otra información que considere relevante para esta actividad.

# referencias:
<debemos siempre reconocer los créditos de partes del código que reutilizaremos, así como referencias a youtube, o referencias bibliográficas utilizadas para desarrollar el proyecto o la actividad>
## sitio1-url 
## sitio2-url
## url de donde tomo info para desarrollar este proyecto

#### versión README.md -> 1.0 (2022-agosto)
