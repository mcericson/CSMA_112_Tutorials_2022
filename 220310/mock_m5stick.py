import random

def set_screen_color(r, g, b):
    print("Screen color set to {},{},{}".format(r, g, b))


def read_accelerometer(normalized=False):
    return random.random(), random.random(), random.random()


def print_to_screen(msg, x, y):
   output_msg = "Printing {} at {}, {}" .format(msg, x, y)
   print(output_msg)