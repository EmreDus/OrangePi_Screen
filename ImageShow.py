# Requirements: pip3 install spidev, pip3 install pillow, pip3 install numpy (or) sudo apt-get install python3-numpy, 
#               sudo git clone https://github.com/nvl1109/orangepi_zero_gpio.git => cd orangepi_zero_gpio => sudo python3 setup.py install

from PIL import Image
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

# Load image
image = Image.open("example.jpg")
image = image.convert("1")
# Resize the image to fit the screen
image = image.resize((128, 128), resample=Image.Resampling.LANCZOS)
# Convert the image to an array of RGB pixels
pixels = np.array(image.convert('RGB')).astype(np.uint16)

# Convert the RGB pixels to 16-bit color values
color = ((pixels[:, :, 0] & 0xF8) << 8) | ((pixels[:, :, 1] & 0xFC) << 3) | (pixels[:, :, 2] >> 3)

# Display image
gpio.output(CS, gpio.LOW)   # Set CS pin to low
gpio.output(RST, 1)
gpio.output(DC, 1)
spi.writebytes([0x00, 0x10])
gpio.output(DC, 0)

for i in range(color.shape[0]):
    spi.xfer2(color[i].to_bytes(2, byteorder='big'))

gpio.output(CS, gpio.HIGH)  # Set CS pin to high

# Close SPI
spi.close()