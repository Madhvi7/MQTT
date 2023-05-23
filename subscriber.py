"""Creating a python subscriber"""

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("My First MQTT Program")


def on_message(client, userdata, msg):
    print("Received message: " + str(msg.payload.decode()))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost")
client.loop_forever()
