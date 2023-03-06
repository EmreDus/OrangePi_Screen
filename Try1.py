# Requirements: pip3 install adafruit-blinka , pip3 install adafruit-circuitpython-st7735

import busio
import adafruit_st7735r as st7735

from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector

gpio.init()

spi = busio.SPI(clock=port.PA14, MOSI=port.PA15)

cs_pin = port.PA13
dc_pin = port.PA1
reset_pin = port.PA0

display = st7735.ST7735R(spi, cs=cs_pin, dc=dc_pin, rst=reset_pin, width=128, height=128, colstart=2, rowstart=1)

display.fill(st7735.BLACK)
display.pixel(10, 10, st7735.WHITE)
display.text("Hello, world!", 0, 0, st7735.WHITE)
display.show()
