import m5stick as stick
#import mock_m5stick as stick
import tools
import time



class ColorSpaceRGB(object):

    def __init__(self, x_dim=255, y_dim=255, z_dim=255):

        self.x_dim = x_dim
        self.y_dim = y_dim
        self.z_dim = z_dim

    def get_rgb(self, x, y, z):

        r = int(round(float(x) / self.x_dim * 255))
        g = int(round(float(y) / self.y_dim * 255))
        b = int(round(float(z) / self.z_dim * 255))

        return r, g, b


room =  tools.Cube(10.0, 10.0, 8.0)
color_space = ColorSpaceRGB(room.x_dim, room.y_dim, room.z_dim)

while True:
    ax, ay, az = stick.read_accelerometer(True)
    x, y, z = room.evaluate_point(ax, ay, az)
    r, g, b = color_space.get_rgb(x, y, z)
    stick.set_screen_color(r, g, b)
    time.sleep(0.05)


