#We will import these two definitions from the modules that Ewan created last week
#The sketch will repeat what we did in processing on day 1, but now with the m5stick
#Be warned...This is slow program.

#I have included the commented code for reference.

#def rgb_to_hex(r, g, b):
    #return '%02x%02x%02x' % (r, g, b)

#def remap(value, source_min, source_max, target_min, target_max):
    #return (target_max - target_min) * (value - source_min) / (source_max - source_min) + target_min


from m5stick import rgb_to_hex
from tools import remap

def rgb_screen(width, height):
    for i in range(width):
        for j in range(height):
            r = int(remap(i, 0, width, 0, 255))
            g = int(remap(j, 0, height, 0, 255))
            hex = rgb_to_hex(r,g,0)
            lcd.pixel(i,j,int("0x" + hex))

#clear the screen
lcd.clear()

#get the width and height of the screen
width, height = lcd.screensize()

#set each pixel of the screen in relation to the RGB cube.
rgb_screen(width, height)