x_dim = 500
y_dim = 500
color_mode = HSB

cube_dim = 10
model_scale = 5
render = P3D

color_max_val = cube_dim

if color_mode == HSB:
    #where a,b,c = h,s,v
    a_val = 360
    b_val = 20
    c_val = 10
    
if color_mode == RGB:
    #where a, b, c = r,g,b
    a_val = color_max_val
    b_val = color_max_val
    c_val = color_max_val
    
    

def update_agent_location(x_norm,y_norm):
    global agent_x, agent_y
    
    agent_x = x_norm * x_dim
    agent_y = y_norm * y_dim
    
def get_current_rgb_values():
    
    r = agent_x * (color_max_val/x_dim)
    g = agent_y * (color_max_val/y_dim)
    b = 0
    
    
    return r, g, b

def rgb_background(r,g,b):
    background(r,g,b)

def rgb_cube(agent_x,agent_y,adjusted_level):
    
    background(agent_x,agent_y,cube_dim)
    translate(agent_x,agent_y)
    scale(model_scale)
    angle= radians(frameCount + adjusted_level)
    
    rotateX(angle)
    rotateY(angle)
    
    for i in range(cube_dim):
        for j in range(cube_dim):
            for p in range(cube_dim):
            
                x0 = i
                y0 = j
                z0 = p
            
                r = i
                g = j
                b = p
                
                stroke(r,g,b)
                point(x0,y0,z0)
  

def hsv_cylinder(agent_x,agent_y,adjusted_level): 
    background(360,agent_x,agent_y)
    translate(agent_x,agent_y)
    scale(model_scale)
    angle= radians(frameCount + adjusted_level)
    
    rotateX(angle)
    rotateY(angle)
    
    noStroke()
    for i in range(a_val):
        angle = radians(i)
        for j in range(b_val):
            x = cos(angle)*j
            y = sin(angle)*j
            for p in range(c_val):

                z = p
            
                h = i
                s = j
                v = p
            
                stroke(h,s,v)
                point(x,y,z)
    
                                  
    
    
