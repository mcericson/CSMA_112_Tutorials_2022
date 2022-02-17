x_dim = 500
y_dim = 500
color_mode = HSB
radius_max = x_dim/3
v_val = 100

def set_color_mode():
    #colorMode() = processing environment only
    colorMode(color_mode, 360, radius_max, v_val)


def update_agent_location(angle_norm,radius_norm):
    global angle_deg, radius
    
    angle_deg = angle_norm*360
    radius =  abs(dist(x_dim/2, y_dim/2,mouseX,mouseY))#radius_norm * radius_max
    
def get_agent_location():
    
    agent_x = x_dim/2 + cos(radians(angle_deg)) * radius
    agent_y = y_dim/2 + sin(radians(angle_deg)) * radius
    
    return agent_x, agent_y

def get_agent_location_color():
    
    h = angle_deg
    s = radius
    v = v_val

    #color()  = processing environment only
    return color(h, s, v)

def get_color_values():
    
    proc_color = get_agent_location_color()
    
    h = round(hue(proc_color),2)
    s = round(saturation(proc_color),2)
    v = round(brightness(proc_color),2)
    
    return h,s,v

def get_white():
    
    #color()  = processing environment only
    return color(0, 0, 100)
