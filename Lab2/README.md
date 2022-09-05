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

La arquitectura básica de una cola de mensajes es simple. Hay aplicaciones clientes, llamadas productores, que crean mensajes y los entregan al intermediario (la cola de mensajes). Otras aplicaciones, llamadas consumidores, se conectan a la cola y se suscriben a los mensajes que se procesarán

![image](https://user-images.githubusercontent.com/53051440/188488507-277de476-11e2-4738-9e2a-91fb3fcab3b4.png)



# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

- Lenguaje: Python3
- Librerias: pika, json, time, requests

## IP o nombres de dominio en nube o en la máquina servidor.

-  IP: 3.219.19.187


## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
   -  PUERTO: 15672
   -  USER: user
   -  PASSWORD: password

## como se compila y ejecuta.
   - Para lanzar el serivor
   ``` 
    $ sudo docker start rabbit-server
   ```
   ![image](https://user-images.githubusercontent.com/53051440/188488945-b7c518e4-a298-4633-ad49-32ede344841e.png)
   - Verificamos que el servidor esta corriendo
   ``` 
    $ docker ps
   ```
   ![image](https://user-images.githubusercontent.com/53051440/188489063-fa00a476-533b-4113-ace4-55d6d3aed6fe.png)
   
   - Escribimos la ip en el buscador seguido del puerto por el que rabbitmq escucha. Ingresamos con el usuario y contraseña por defecto 
   ![image](https://user-images.githubusercontent.com/53051440/188489708-026a7e4e-f82b-4b12-a6f9-e83220290241.png)
   
   ![image](https://user-images.githubusercontent.com/53051440/188489792-35607d57-08db-4a80-bcd9-0315519d16e4.png)
   
   - Para comenzar a producir los datos del simuladot IOT abrimos una terminal y ejecutamos
      Este archivo genera datos aleatorios y los envia al mom
   
   ``` 
    $ python3 producer.py
   ```
   ![image](https://user-images.githubusercontent.com/53051440/188490640-d1790027-9250-4831-9bf8-09090aa31e12.png)
   
   configuracion de parametros
   
   ![image](https://user-images.githubusercontent.com/53051440/188492568-735cc5f7-8c7f-4f43-962f-b351c3f7bf09.png)


   - Para comenzar a recibir los datos del simulador IOT abrimos una terminal y ejecutamos 
      Este archivo recibe los datos que estan encolados en el mom, los recibe en consola y los envia al simulador ubidots
   
   ``` 
    $ python3 consumer.py
   ```
   ![image](https://user-images.githubusercontent.com/53051440/188490820-e6cd693f-a1dc-4b37-b975-2875f38e632b.png)

   
   en este mismo archivo se encuentra el vinculo con ubidots para comenzar a enviar los datos al simulador que se encuentra en:
   
   ```
      https://stem.ubidots.com/app/dashboards/public/widget/y_A6_v39MSv3p00rpoQe0b0UIBFaLye53YKdWyaYI2o
   ```
![image](https://user-images.githubusercontent.com/53051440/188490985-f384b628-039b-4647-9596-07f7e31fa15e.png)

# referencias:

## https://blog.bi-geek.com/rabbitmq-para-principiantes/#:~:text=%C2%BFC%C3%B3mo%20funciona%3F,los%20mensajes%20que%20se%20procesar%C3%A1n
## https://help.ubidots.com/en/articles/569964-simulate-data-in-ubidots-using-python

#### versión README.md -> 1.0 (2022-septiembre)
