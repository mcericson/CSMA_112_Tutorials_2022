x_dim = 500
y_dim = 500
color_mode = RGB
color_max_value = x_dim


def set_color_mode():
    """Sets the Processing color mode."""
    colorMode(RGB, color_max_value)


def get_agent_location(x_norm, y_norm, z_norm=0.0):
    """Converts normalized coordinates to x,y coordinate."""
    agent_x = x_norm * x_dim
    agent_y = y_norm * y_dim
    return agent_x, agent_y
    
    
def get_agent_location_color(agent_x, agent_y):
    """Converts an x,y coordinate into a Processing color."""
    r = agent_x * (color_max_value/x_dim)
    g = agent_y * (color_max_value/y_dim)
    b = 0
    return color(r, g, b)


def get_white():
    """Gets a white Processing color object."""
    return color(color_max_value)
