# Requirements: pip3 install adafruit-blinka , pip3 install adafruit-circuitpython-st7735

import board
import busio
import displayio
from adafruit_st7735r import ST7735R

cs_pin = board.D13 
dc_pin = board.D1
reset_pin = board.D0

# Initialize SPI bus
spi = busio.SPI(board.SCK, MOSI=board.MOSI)

# Initialize display
display = adafruit_st7735r.ST7735R(spi, cs=cs_pin, dc=dc_pin, rst=reset_pin, width=128, height=128, colstart=2, rowstart=1)

# Draw a rectangle and some text on the display
display.fill(st7735.BLACK)
display.rectangle(10, 10, 30, 30, st7735.WHITE)
display.text("Hello, world!", 0, 0, st7735.WHITE)

# Update the display
display.show()
