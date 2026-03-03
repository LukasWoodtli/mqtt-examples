
import os.path
import paho.mqtt.client as mqtt
import logging

mqtt_server_host = "mosquitto-host"
mqtt_server_port = 1883
mqtt_keepalive = 60

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("python-mqtt-client")

def on_connect(client, userdata, flags, rc):
    print("Result from connect: {}".format(
        mqtt.connack_string(rc)))
    # Subscribe to the vehicles/vehiclepi01/tests topic filter
    client.subscribe("vehicles/vehiclepi01/tests", qos=2)

def on_subscribe(client, userdata, mid, granted_qos):
    print("I've subscribed with QoS: {}".format(
        granted_qos[0]))

def on_message(client, userdata, msg):
    print("Message received. Topic: {}. Payload: {}".format(
        msg.topic, 
        str(msg.payload)))


if __name__ == "__main__":
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    
    logger.info(f"Connecting to MQTT server at {mqtt_server_host}:{mqtt_server_port} with keepalive {mqtt_keepalive}...")
    client.connect(host=mqtt_server_host,
        port=mqtt_server_port,
        keepalive=mqtt_keepalive)
    client.loop_forever()
