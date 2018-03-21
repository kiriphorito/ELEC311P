import time
import datetime
import json

from random import *

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

MCP3008_SAMPLING = 200 # at 5V
SAMPLE_WINDOW = 50 # in mS

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

device1 = {
    'id': '1',
    'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'mic_reading': randint(50,100),
    'image': 'test-image1'
}

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

    return mic_voltage_max - mic_voltage_min

def print_sound_bars(sound_range):
    steps_range = 10
    steps = sound_range // steps_range
    for x in range(0, steps):
        print("X", end="", flush=True)
    print()

# Main program loop.
while True:
    # Start from lowest possible value and highest for min and max
    # mic_voltage_min = 1024 # MCP3008 is a 10-bit chip
    # mic_voltage_max = 0

    # Start from initial values, i.e. initialise both values to the first value

    min_volume = get_voltage_aplitude()
    max_volume = min_volume
    mean_volume = min_volume
    # print_sound_bars(min_volume)

    step_space = 100

    for x in range(0, step_space):
        mic_volume = get_voltage_aplitude()
        mean_volume += mic_volume
        # print_sound_bars(mic_volume)
        if (mic_volume < 1024 and mic_volume >= 0): # To filter out wrong vaules
            if mic_volume > max_volume:
                max_volume = mic_volume
            elif mic_volume < min_volume:
                mic_volume = mic_volume

    volume_range = max_volume - min_volume
    mean_volume /= step_space
    distance_from_mean = mean_volume - (volume_range/2)
    #volts = (signal_range * 5.0) / 1024

    print("Level Difference:", volume_range, end="", flush=True)
    if distance_from_mean > 50:
        print("    Unexpected sound", volume_range, end="", flush=True)
    print()


    # time.sleep(1/SAMPLE_WINDOW)
