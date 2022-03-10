import math


def euclidean_distance_2D(x0, y0, x1, y1):
    return math.sqrt((x0-x1)**2 + (y0-y1)**2)


def clamp(val, min_val, max_val):
    if val < min_val: return min_val
    if val > max_val: return max_val
    return val


def remap(value, source_min, source_max, target_min, target_max):
    return (target_max - target_min) * (value - source_min) / (source_max - source_min) + target_min


def normalize(value, source_min, source_max):
    return remap(value, source_min, source_max, 0.0, 1.0)


def angle_between_2D(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang


# https://stackoverflow.com/questions/24852345/hsv-to-rgb-color-conversion
def hsv_to_rgb(h, s, v):
    if s == 0.0: v*=255; return (v, v, v)
    i = int(h*6.)
    f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
    v = int(v)
    t = int(t)
    p = int(p)
    q = int(q)
    if i == 0: return (v, t, p)
    if i == 1: return (q, v, p)
    if i == 2: return (p, v, t)
    if i == 3: return (p, q, v)
    if i == 4: return (t, p, v)
    if i == 5: return (v, p, q)


class Cube(object):

    def __init__(self, x_dim, y_dim, z_dim):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.z_dim = z_dim

    def evaluate_point(self, xn, yn, zn):
        return self.x_dim * xn, self.y_dim * yn, self.z_dim * zn
    
    

