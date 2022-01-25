
# Settings (defaults)
x_dim = 500
y_dim = 500
flashlight_diameter = 50
bg_color = 0
color_mode = RGB

# System state
agent_x = 0
agent_y = 0
    

def get_agent_color():
    r = agent_x
    g = agent_y
    b = 0 # Use a constant value for blue
    return r, g, b
