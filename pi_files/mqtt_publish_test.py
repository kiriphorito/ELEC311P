import paho.mqtt.publish as publish

MQTT_SERVER = "broker.mqttdashboard.com:8000"
MQTT_PATH = "testtopic/nhm"

publish.single(MQTT_PATH, "Hello World!", hostname = MQTT_SERVER)
