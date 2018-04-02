import paho.mqtt.client as mqtt
import time
import datetime
import json

from random import *
from picamera import PiCamera

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

MCP3008_SAMPLING = 200000 # at 5V
SAMPLE_WINDOW = 500 # in mS

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
# SPI_PORT   = 0
# SPI_DEVICE = 0
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


def get_voltage_aplitude():
    # Start from lowest possible value and highest for min and max
    # mic_voltage_min = 1024 # MCP3008 is a 10-bit chip
    # mic_voltage_max = 0

    # Start from initial values, i.e. initialise both values to the first value
    mic_voltage_min = mcp.read_adc(0)
    mic_voltage_max = mic_voltage_min

    samples_per_window = MCP3008_SAMPLING//SAMPLE_WINDOW
    for x in range(0, samples_per_window):
        mic_voltage = mcp.read_adc(0)
        if (mic_voltage < 1024 and mic_voltage >= 0): # To filter out wrong vaules
            if mic_voltage > mic_voltage_max:
                mic_voltage_max = mic_voltage
            elif mic_voltage < mic_voltage_min:
                mic_voltage_min = mic_voltage
        # print(mic_voltage)
        time.sleep(1/MCP3008_SAMPLING)
    print_sound_bars(mic_voltage_max - mic_voltage_min)
    # print(mic_voltage_max - mic_voltage_min)
    return mic_voltage_max - mic_voltage_min

def print_sound_bars(sound_range):
    steps_range = 10
    steps = sound_range // steps_range
    for x in range(0, steps):
        print("X", end="", flush=True)
    print()

# Main program loop.
while True:

    get_voltage_aplitude()
