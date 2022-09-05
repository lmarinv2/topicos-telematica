import pika
import json
import time
import requests

#parametros
label= 'temperatura' #label del dispositivo en ubidots
label_device = "lab2" # dispositvo en ubidots
token = 'BBFF-YdfB2Fi65wPEew7wGtoVO3A4EBpEhS' #token del dispositivo de ubidots
ip='3.219.19.187' # ip de la instancia
user ="user" # usuario para acceder a rabbitmq
password = "password"  #contraseña para accerder a rabbitmq

connection = pika.BlockingConnection(pika.ConnectionParameters(ip, 5672, '/', pika.PlainCredentials(usuario, password")))
channel = connection.channel()

def callback(ch, method, properties, body):
    print(f'Temperatura : {json.loads(body)} is received')
    payload = {label : body.decode(encoding='UTF-8')}
    print(payload)
    post_request(payload)

def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, label_device)
    headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    print("Puede ver las grafica https://stem.ubidots.com/app/dashboards/public/widget/y_A6_v39MSv3p00rpoQe0b0UIBFaLye53YKdWyaYI2o")
    return True
    time.sleep(1)

channel.basic_consume(queue="datos", on_message_callback=callback, auto_ack=True)
channel.start_consuming()
