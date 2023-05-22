"""Creating a python publisher"""

import paho.mqtt.client as mqtt


def on_connect(rc):
    print("Connected with result code " + str(rc))


client = mqtt.Client()
client.on_connect = on_connect

client.connect("localhost")
client.loop_start()

while True:
    message = input("Enter message to publish (or 'q' to quit): ")

    if message.lower() == 'q':
        break
    client.publish("My First MQTT Program", message)

client.loop_stop()
client.disconnect()
