import spidev
import Adafruit_ST7735 as ST7735

# Raspberry Pi pin configuration for SPI
SCK = 14    # GPIO14, physical pin 23
SDA = 15    # GPIO15, physical pin 19
A0 = 1      # GPIO1, physical pin 11
RESET = 0   # GPIO0, physical pin 13
CS = 13     # GPIO13, physical pin 24

# Create SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)

# Initialize display
disp = ST7735.ST7735(
    spi=spi,
    cs=CS,
    dc=A0,
    rst=RESET,
    width=128,
    height=160
)
disp.begin()

# Clear display
disp.clear()

# Draw text
disp.draw_text(0, 0, "Hello, world!", ST7735.Color565(255, 255, 255))

# Update display
disp.display()

# Close SPI bus
spi.close()
