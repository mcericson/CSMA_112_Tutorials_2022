x_dim = 500
y_dim = 500
color_mode = HSB
h_val, s_val, v_val = 360,x_dim/3 ,10
color_max_value =  h_val, s_val, v_val
current_h_val = 1.0

scale_val = x_dim/3/s_val

def update_agent_location(x_norm,y_norm):
    
    global agent_x, agent_y

    translate(x_dim/2,y_dim/2)



    angle = radians(current_h_val)
    agent_x = cos(angle)*s_val
    agent_y = sin(angle)*s_val
    


    

def get_current_color_values():
    
    angle = radians(current_h_val)
    
    h = cos(angle)*s_val
    s = sin(angle)*s_val
    v = v_val
    
    return h, s, v
