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
   
   ``` 
    $ python3 producer.py
   ```
   
   -Para comenzar a recibir los datos del simulador IOT abrimos una terminal y ejecutamos 
   
    ``` 
    $ python3 consumer.py
   ```
   
   en este mismo archivo se encuentra el vinculo con ubidots para comenzar a enviar los datos al simulador que se encuentra en:
   
   ```
      https://stem.ubidots.com/app/dashboards/public/widget/y_A6_v39MSv3p00rpoQe0b0UIBFaLye53YKdWyaYI2o
   ```



# 5. otra información que considere relevante para esta actividad.

# referencias:
<debemos siempre reconocer los créditos de partes del código que reutilizaremos, así como referencias a youtube, o referencias bibliográficas utilizadas para desarrollar el proyecto o la actividad>
## sitio1-url 
## sitio2-url
## url de donde tomo info para desarrollar este proyecto

#### versión README.md -> 1.0 (2022-agosto)
