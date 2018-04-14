import paho.mqtt.client as mqttClient
import time
import datetime
import json

def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("Connected to broker")

        global Connected                #Use global variable
        Connected = True                #Signal connection

    else:

        print("Connection failed")

def on_message(client, userdata, message):
    json_data = json.loads(message.payload)
    data = str(json_data["time"]) + " " + str(json_data["mean_reading"])
    file = open("records.txt","a")
    file.write(data+"\n")
    file.close()
    print(data)

Connected = False   #global variable for the state of the connection

client = mqttClient.Client("Python")               #create new instance
client.username_pw_set("qufzpimd","ra44TqXIg1PZ")    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback

client.connect("m23.cloudmqtt.com",10952,60)          #connect to broker

client.loop_start()        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(0.1)

client.subscribe("ELEC311P-device1")

try:
    while True:
        time.sleep(0.5)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
