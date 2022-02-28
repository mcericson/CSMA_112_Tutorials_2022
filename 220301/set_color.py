from m5stack import *
from m5ui import *
from uiflow import *
import time


def color_pause(color,duration):
    
    setScreenColor(color)
    lcd.text(10,10, "A", transparent=False)
    time.sleep_ms(duration)
    


def flash_rgb(duration, stop):
    count = 0
    while count < stop:
        
        count += 1
        color_pause(0xff0000,duration)
        color_pause(0x00ff00, duration)
        color_pause(0x0000ff, duration)