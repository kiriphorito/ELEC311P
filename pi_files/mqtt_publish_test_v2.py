import paho.mqtt.client as mqtt
import time
data = "Hello from Raspberry Pi!"
while True:


print(data)
try:
    client=mqtt.Client()
    client.username_pw_set("qufzpimd","ra44TqXIg1PZ")
    client.connect("m23.cloudmqtt.com",10952,60)
    client.publish("nhm",data)
    time.sleep(1)
except KeyboardInterrupt:
    print("end")
    client.disconnect()
