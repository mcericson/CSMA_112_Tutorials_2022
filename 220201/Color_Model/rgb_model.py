x_dim = 500
y_dim = 500
color_mode = RGB
r_val = x_dim
g_val = x_dim
b_val = x_dim
color_max_value = r_val, g_val, b_val



def update_agent_location(x_norm,y_norm):
    global agent_x, agent_y
    
    agent_x = x_norm * x_dim
    agent_y = y_norm * y_dim
    
def get_current_color_values():
    
    r = agent_x * (r_val/x_dim)
    g = agent_y * (g_val/y_dim)
    b = 0
    
    return r, g, b
