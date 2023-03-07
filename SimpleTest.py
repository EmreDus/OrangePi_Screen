# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
 
"""
 This test will initialize the display using displayio and draw a solid green
 background, a smaller purple rectangle, and some yellow text.
"""

import board
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R

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

# Release any resources currently in use for the displays
displayio.release_displays()

spi = busio.SPI(clock=port.PA14, MOSI=port.PA15)

tft_cs = port.PA13
tft_dc = port.PA1

#spi = board.SPI()
#tft_cs = board.D5
#tft_dc = board.D6

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=port.PA0
)

display = ST7735R(display_bus, width=128, height=128, colstart=2, rowstart=1)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(128, 128, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00  # Bright Green

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(108, 108, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xAA0088  # Purple
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=10, y=10)
splash.append(inner_sprite)

# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=30, y=64)
splash.append(text_area)

while True:
    pass