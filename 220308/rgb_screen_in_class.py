from m5stick import rgb_to_hex
from tools import remap

#def rgb_to_hex(r, g, b):
    #return '%02x%02x%02x' % (r, g, b)

#def remap(value, source_min, source_max, target_min, target_max):
    #return (target_max - target_min) * (value - source_min) / (source_max - source_min) + target_min

def rgb_screen(width, height):
    for i in range(width):
        for j in range(height):
            x = i
            y = j
            r = int(remap(i, 0, width, 0, 255))
            g = int(remap(j, 0, height, 0, 225))
            hex = rgb_to_hex(r, g, 0)
            lcd.pixel(x, y, int("0x" + hex))

lcd.clear()

width, height = lcd.screensize()

rgb_screen(width, height)