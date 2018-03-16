import paho.mqtt.client as mqtt
import time
import sys
import json
import datetime
from random import *

device1 = {
    'id': '1',
    'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'mic_reading': randint(50,100),
    'image': 'test-image1'
}

device2 = {
    'id': '2',
    'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'mic_reading': randint(50,100),
    'image': 'test-image2'

}

print("Script started, sending data........")

while True:
    device1['time'] =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    device2['time'] =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    device1['mic_reading'] = randint(50,100)
    device2['mic_reading'] = randint(50,100)

    print(json.dumps(device1))
    print(json.dumps(device2))

    try:
        client=mqtt.Client()
        client.username_pw_set("qufzpimd","ra44TqXIg1PZ")
        client.connect("m23.cloudmqtt.com",10952,60)
        client.publish("ELEC311P-device1",json.dumps(device1))
        client.publish("ELEC311P-device2",json.dumps(device2))
        time.sleep(1)
    except KeyboardInterrupt:
        print("CTRL-C.... terminated")
        sys.exit()
        client.disconnect()
