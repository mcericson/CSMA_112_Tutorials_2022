x_dim = 500
y_dim = 500
color_mode = RGB
color_max_value = x_dim


def update_agent_location(x_norm,y_norm):
    global agent_x, agent_y
    
    agent_x = x_norm * x_dim
    agent_y = y_norm * y_dim
    
def get_current_color_values():
    
    r = agent_x * (color_max_value/x_dim)
    g = agent_y * (color_max_value/y_dim)
    b = 0
    
    return r, g, b
