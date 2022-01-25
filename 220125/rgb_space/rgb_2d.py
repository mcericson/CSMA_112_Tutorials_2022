#settings
x_dim = 800
y_dim = 800
render = P2D
color_dim = x_dim
bg_color = x_dim
color_mode = RGB

rot_deg = 0

agent_x = 0
agent_y = 0

def rgb_model():
    

    
    for i in range(agent_x):
        for j in range(agent_y):
            
            x0 = i
            y0 = j
            
            r = i
            g = j
            b = 0
        
            fill(r,g,b)
            rect(x0,y0,1)
            
    
