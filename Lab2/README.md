# ST0263 Tópicos especiales en telemática
# Estudiante: Laura Marin Velez, lmarinv2@eafit.edu.co
# Profesor: Edwin Nelson Montoya, emontoya@eafit.edu.co
#
# Laboratorio 2
#
# 1. Descripcion de la actividad
Uso rabbitmq como MOM simulando eventos IOT en python 

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor
* Adaptacion de Rabbitmq a un pryecto IOT
* Simulador de eventos IOT (ubidots)
* Maquina desplegada en AWS

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

RabbitMQ es middleware de código abierto que va a funcionar como un intermediario entre aplicaciones
que pueden ser independientes entre si. De esta forma, RabbitMQ se constituye en una capa software
que le permitirá la comunicación entre ellas. Una de las grandes ventajas que da el considerar este tipo
de soluciones, es que la arquitectura final del sistema se convierte en una solución débilmente acoplada.

RabbitMQ implementa el protocolo mensajería de capa de aplicación AMQP (Advanced Message Queueing Protocol), el cual está enfocado en la comunicación de mensajes asíncronos con garantía de entrega, a través de confirmaciones de recepción de mensajes desde el broker al productor y desde los consumidores al broker.


# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

Lenguaje: Python3
Librerias: pika, json, time, requests

## como se compila y ejecuta.
    ``` 
    $ sudo docker start rabbit-server
    ```
## detalles del desarrollo.
## detalles técnicos
## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
## opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)
## 
## opcionalmente - si quiere mostrar resultados o pantallazos 

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

# IP o nombres de dominio en nube o en la máquina servidor.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

## como se lanza el servidor.

## una mini guia de como un usuario utilizaría el software o la aplicación

## opcionalmente - si quiere mostrar resultados o pantallazos 

# 5. otra información que considere relevante para esta actividad.

# referencias:
<debemos siempre reconocer los créditos de partes del código que reutilizaremos, así como referencias a youtube, o referencias bibliográficas utilizadas para desarrollar el proyecto o la actividad>
## sitio1-url 
## sitio2-url
## url de donde tomo info para desarrollar este proyecto

#### versión README.md -> 1.0 (2022-agosto)