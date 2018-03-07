import time
import os
from picamera import PiCamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
pin = 7
GPIO.setup(pin, GPIO.IN)
counter = 0

camera = PiCamera()

while 1:
    counter += 1
    print(counter)
    if GPIO.input(pin) == GPIO.HIGH:
        print("I heard something!")
        camera.capture("image-%s.jpg" % counter)
    time.sleep(0.5)
