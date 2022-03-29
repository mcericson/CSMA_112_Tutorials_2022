from m5ui import setScreenColor
from m5stack import btnA
from m5stack import lcd
from m5ui import setScreenColor
import imu
import m5ui
import unit


my_imu = imu.IMU()

sonar = None


def read_sonar_distance(inches=True):
    global sonar
    if sonar is None: # Lazy-loading of sensor (only when needed)
        sonar = unit.get(unit.ULTRASONIC, unit.PORTA)
    dist = sonar.distance
    if inches:
        dist = dist / 25.4 # Convert from mm to in
    return int(round(dist))


def set_screenColor(r, g, b):
    hex_color = int('%02x%02x%02x' % (r, g, b))
    setScreenColor(hex_color)


def erase_screen():
    set_screenColor(0, 0, 0)

def display_message(msg):
    lcd.clear()
    lcd.text(0, 0, str(msg))

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


class SampleBuffer(object):

    def __init__(self, size=10):
        self.size = size
        self.samples = []
    
    def add(self, sample):
        if len(self.samples) == self.size:
            self.samples.pop(0)
        self.samples.append(sample)
    
    def mean(self):
        return sum(self.samples) / float(len(self.samples))
