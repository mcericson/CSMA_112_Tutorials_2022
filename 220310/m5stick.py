from m5ui import setScreenColor
from m5stack import btnA
from m5stack import lcd
from m5ui import setScreenColor
import imu
import m5ui

my_imu = imu.IMU()


def set_screen_color(r, g, b):
    hex_color = int('%02x%02x%02x' % (r, g, b))
    setScreenColor(hex_color)

def erase_screen():
    set_screen_color(0, 0, 0)

def display_message(msg):
    lcd.text(0, 0, msg)

def button_pressed():
    return btnA.wasPressed() 


def rgb_to_hex(r, g, b):
    return '%02x%02x%02x' % (r, g, b)


def read_accelerometer(normalized=False):
    x, y, z = my_imu.acceleration
    if normalized: # defaults range from -1.0 to 1.0 but sometimes exceed this boundary
        x = (x + 1.0) / 2.0
        y = (y + 1.0) / 2.0
        z = (z + 1.0) / 2.0
        x = clamp(x, 0.0, 1.0)
        y = clamp(y, 0.0, 1.0)
        z = clamp(z, 0.0, 1.0)
    return x, y, z


def clamp(val, min_val, max_val):
    if val < min_val: return min_val
    if val > max_val: return max_val
    return val


def set_screen_color(r, g, b):
    hex_color = rgb_to_hex(r, g, b)
    screen_color = int('0x' + (hex_color))
    setScreenColor(screen_color)


def print_to_screen(msg, x, y):
    lcd.print(msg, x, y)
