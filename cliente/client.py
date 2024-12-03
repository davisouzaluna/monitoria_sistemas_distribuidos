import socket
import threading
import time
from json_manipulator import JSONManipulator
from paho.mqtt import client as mqtt_client

#ip_host = '127.0.0.1'
#porta = 10010

MQTT_BROKER = '127.0.0.1'
MQTT_PORT = 1883
client_id = "Davi_Luna"

json_manipulator = JSONManipulator()

def negociacao_topico(ip_host, porta):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    endereco = (ip_host, porta)
    s.connect(endereco)

    #cliente tenta enviar o topico
    topico_enviar = b'monitoriaifpe'
    s.sendall(topico_enviar)
    mensagem= s.recv(1024)
    print(f'{mensagem}')

    # salva em varchar
    TOPIC = mensagem.decode('utf-8')
    print(f'{TOPIC}')

    #retorna pra guardar em var
    return TOPIC


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1,client_id)
    client.on_connect = on_connect
    client.connect(MQTT_BROKER, MQTT_PORT)
    return client


def mqtt_cb(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode("utf-8")
    print(payload)
    
    json_manipulator.createMQTTjson(msg,"teste")

    
def subscribe(client: mqtt_client,topico):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topico)
    client.on_message = mqtt_cb


def run():
    client = connect_mqtt()
    print("teste")

   
    topico= negociacao_topico("127.0.0.1", 15240)
    

    subscribe(client,topico)
    client.loop_forever()

if __name__ == '__main__':
    run()


