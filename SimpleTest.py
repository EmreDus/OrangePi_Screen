from PIL import Image, ImageDraw, ImageFont
import spidev
import numpy as np

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

# Define SPI pins
SPI_PORT = 0
SPI_DEVICE = 0

# Initialize SPI
spi = spidev.SpiDev()
spi.open(SPI_PORT, SPI_DEVICE)
spi.max_speed_hz = 1000000
spi.mode = 0b01   # Set SPI mode to 1

CS = port.PA13
DC = port.PA1
RST = port.PA0

# Create image
image = Image.new("RGB", (128, 128), color="black")
draw = ImageDraw.Draw(image)

# Add text
font = ImageFont.truetype("arial.ttf", size=20)
draw.text((20, 50), "Hello, World!", fill=(255, 255, 255), font=font)

# Convert image to array of RGB pixels
pixels = np.array(image.convert('RGB')).astype(np.uint16)

# Convert RGB pixels to 16-bit color values
color = ((pixels[:, :, 0] & 0xF8) << 8) | ((pixels[:, :, 1] & 0xFC) << 3) | (pixels[:, :, 2] >> 3)

# Display image
gpio.output(CS, gpio.LOW)   # Set CS pin to low
gpio.output(RST, 1)
gpio.output(DC, 1)
spi.writebytes([0x00, 0x10])
gpio.output(DC, 0)

for i in range(color.shape[0]):
    spi.xfer2(color[i].tobytes())

gpio.output(CS, gpio.HIGH)  # Set CS pin to high

# Close SPI
spi.close()
