import spidev
from adafruit_st7735r import ST7735R

from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector

# Orange Pi Zero LTS configuration.
cs = port.PA13 
dc = port.PA1
rst = port.PA0

SPI_PORT = 0
SPI_DEVICE = 1

# Create SPI interface.
spi = spidev.SpiDev()
spi.open(SPI_PORT, SPI_DEVICE)
spi.max_speed_hz = 4000000

# Create LCD class instance.
display = ST7735R(spi, dc=DC, rst=RST)

# Initialize display.
display.begin()

# Clear the screen.
display.fill(0)

# Draw some text on the screen.
display.draw_text('Hello, world!', x=10, y=10, color=(255, 255, 255))

# Update the display.
display.show()