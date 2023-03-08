import OPi.GPIO as GPIO
import displayio
from adafruit_st7735r import ST7735R

GPIO.setmode(GPIO.BOARD)
GPIO.setup(24, GPIO.OUT) # set pin 24 as output

spi = board.SPI()
tft_cs = 17 # set the chip select pin PA13
tft_dc = 8 # set the data/command pin (PA1)

displayio.release_displays()
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=27)

display = ST7735R(display_bus, width=128, height=128, colstart=2, rowstart=1)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(128, 128, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFF0000

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

while True:
    GPIO.output(24, GPIO.HIGH) # turn on LED
    time.sleep(0.5)
    GPIO.output(24, GPIO.LOW) # turn off LED
    time.sleep(0.5)
