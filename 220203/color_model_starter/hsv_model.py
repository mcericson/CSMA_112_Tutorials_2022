x_dim = 500
y_dim = 500
color_mode = HSB
radius_max = x_dim/3
v_val = 100

def set_color_mode():
    colorMode(color_mode, 360, radius_max, v_val)


def update_agent_location(angle_norm, radius_norm):
    global angle_deg, radius
    
    angle_deg = angle_norm*360
    radius    = radius_norm * radius_max
    
def get_agent_location_xy():
    
    agent_x = cos(radians(angle_deg)) * radius + x_dim/2
    agent_y = sin(radians(angle_deg)) * radius + y_dim/2
    
    return agent_x, agent_y
    
    
def get_agent_location_color():
    
    h = angle_deg
    s = radius
    v = v_val 
    
    return color(h,s,v)


def get_white():
    
    return color(0,0,v_val)
    
