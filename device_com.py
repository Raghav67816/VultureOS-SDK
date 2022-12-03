"""
device_com.py
Device communication functions
"""
# Import dependencies

from admin import config_obj
from paho.mqtt import client

mqtt_client = client.Client("BeagleBone")

# On subscribe
def on_subscribe():
    print("Subscribed to topics.")

# On message received
def onMessage(client, userdata, msg):
    decoded_msg = int(msg.payload.decode('utf-8'))
    if decoded_msg > 600:
        mqtt_client.publish("garden_pump", "1")

    else:
        pass

# Connect to broker
def connect_broker():
    def onConnect(client, userdata, msg, tmp=None):
        print("Client connected successfully")

    broker_addr = "192.168.1.37"
    broker_port = 1883

    # Set callbacks
    mqtt_client.on_connect = onConnect
    mqtt_client.on_message = onMessage

    print(f"Connecting to {broker_addr}....")
    mqtt_client.connect(broker_addr, broker_port)
    mqtt_client.subscribe("garden")
    mqtt_client.loop_forever()

connect_broker()