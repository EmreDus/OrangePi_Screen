# Requirements: pip3 install adafruit-blinka , pip3 install adafruit-circuitpython-st7735

import busio
import adafruit_st7735r as st7735
import numpy as np
from PIL import Image, ImageDraw

from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector

# Set up the pins as outputs
gpio.init()
gpio.setcfg(port.PA14, gpio.OUTPUT)  # Clock
gpio.setcfg(port.PA15, gpio.OUTPUT)  # MOSI
gpio.setcfg(port.PA13, gpio.OUTPUT)  # CS
gpio.setcfg(port.PA1, gpio.OUTPUT)   # DC
gpio.setcfg(port.PA0, gpio.OUTPUT)   # Reset

spi = busio.SPI(clock=port.PA14, MOSI=port.PA15)

cs_pin = port.PA13
dc_pin = port.PA1
reset_pin = port.PA0

display = st7735.ST7735R(spi, cs=cs_pin, dc=dc_pin, rst=reset_pin, width=128, height=128, colstart=2, rowstart=1)

# Load the image file
image = Image.open("example.jpg")
# Resize the image to fit the screen
image = image.resize((128, 128), Image.ANTIALIAS)
# Convert the image to an array of RGB pixels
pixels = np.array(image.convert('RGB')).astype(np.uint16)

# Convert the RGB pixels to 16-bit color values
color = ((pixels[:, :, 0] & 0xF8) << 8) | ((pixels[:, :, 1] & 0xFC) << 3) | (pixels[:, :, 2] >> 3)

# Display the image on the screen
display._write_command(st7735.CASET)
display._write_data(bytes([2, 2, 129, 129]))
display._write_command(st7735.RASET)
display._write_data(bytes([1, 2, 129, 130]))
display._write_command(st7735.RAMWR)
display._write_data(color.tobytes())

display.show()