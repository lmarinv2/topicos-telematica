# https://medium.com/better-programming/introduction-to-message-queue-with-rabbitmq-python-639e397cb668
# producer.py
# This script will publish MQ message to my_exchange MQ exchange
import random
import pika
import time

#Constantes
n=0 #numero de datos que envia
ip= '3.219.19.187' # direccion ip de la instancia
user= 'user' #ususario para accerder a rabbitmq
password = 'password' #contraseña para accerder a rabbitmq

connection = pika.BlockingConnection(pika.ConnectionParameters(ip, 5672, '/', pika.PlainCredentials(user, password)))
channel = connection.channel()

while(n<50):
        datos = str(random.randint(75, 90))
        channel.basic_publish(exchange='lab2', routing_key='temp', body=datos)
        print('dato temperatura enviado')
        n=n+1
        time.sleep(5)

connection.close()
