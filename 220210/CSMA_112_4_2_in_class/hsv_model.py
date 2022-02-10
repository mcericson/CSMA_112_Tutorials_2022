import math

x_dim = 500
y_dim = 500
color_mode = HSB
radius_max = x_dim/3
v_val = 100


def set_color_mode():
    """Sets the Processing color mode."""
    colorMode(color_mode, 360, radius_max, v_val) # Processing environment only


def get_agent_location(angle_norm, radius_norm):
    """Converts normalized angle and radius to x,y coordinate."""
    angle_deg = angle_norm * 360
    radius =  radius_norm * radius_max
    agent_x = x_dim/2 + cos(radians(angle_deg)) * radius
    agent_y = y_dim/2 + sin(radians(angle_deg)) * radius
    return agent_x, agent_y


def get_agent_location_color(agent_x, agent_y):
    """Converts an x,y coordinate into a Processing color."""
    center_x, center_y = x_dim/2, y_dim/2
    x_axis = (center_x+1, center_y)
    angle_deg = angle_between((agent_x, agent_y), (center_x, center_y), x_axis)
    radius = dist(agent_x, agent_y, center_x, center_y)
    h, s, v = angle_deg, radius, v_val
    return color(h, s, v) # Processing environment only


def get_white():
    """Gets a white Processing color object."""
    return color(0, 0, 100) # Processing environment only


def angle_between(a, b, c):
    """Computes the angle between vectors ba and bc"""
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang
