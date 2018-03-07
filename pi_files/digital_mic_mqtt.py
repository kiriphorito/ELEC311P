import time
import os
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

from picamera import PiCamera

GPIO.setmode(GPIO.BOARD)
pin = 7
GPIO.setup(pin, GPIO.IN)
counter = 0

camera = PiCamera()

while 1:
    counter += 1
    print(counter)
    if GPIO.input(pin) == GPIO.HIGH:
        data = counter + " - I heard something!"
        print("I heard something!")
        camera.capture("image-%s.jpg" % counter)
        try:
            client=mqtt.Client()
            client.username_pw_set("qufzpimd","ra44TqXIg1PZ")
            client.connect("m23.cloudmqtt.com",10952,60)
            client.publish("nhm",data)
            time.sleep(1)
        except KeyboardInterrupt:
            print("end")
            client.disconnect()
    time.sleep(0.5)
