# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time

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

# Hardware SPI configuration:
# SPI_PORT   = 0
# SPI_DEVICE = 0
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
print('-' * 57)
# Main program loop.
while True:
    mic_voltage_min = 1024 # MCP3008 is a 10-bit chip
    mic_voltage_max = 0

    samples_per_window = MCP3008_SAMPLING//SAMPLE_WINDOW
    for x in range(0, samples_per_window):
        mic_voltage = mcp.read_adc(0)
        if (mic_voltage < 1024):
            if mic_voltage > mic_voltage_max:
                mic_voltage_max = mic_voltage
            elif mic_voltage < mic_voltage_min:
                mic_voltage_min = mic_voltage
        print(mic_voltage)

    signal_range = mic_voltage_max - mic_voltage_min
    volts = (signal_range * 5.0) / 1024

    # Read all the ADC channel values in a list.
    #values = [0] * 8
    #for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
        #values[i] = mcp.read_adc(i)
    # Print the ADC values.
    #print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    # print(volts)
    time.sleep(1/SAMPLE_WINDOW)
