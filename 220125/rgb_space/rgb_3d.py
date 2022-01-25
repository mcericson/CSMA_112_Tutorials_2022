#settings

x_dim = 800
y_dim = 800
render = P3D
color_dim = 20
bg_color = color_dim
color_mode = RGB
cube_scale = 10
rot_deg = 0

agent_x = 0
agent_y = 0


def rgb_model():
    translate(agent_x, agent_y)
    
    rot_rad = radians(rot_deg)
    
    rotateX(rot_rad)
    rotateY(rot_rad)
    rotateZ(rot_rad)

    scale(cube_scale)
    strokeCap(SQUARE)
    strokeWeight(2)
    
    
    
    for i in range(agent_x/cube_scale):
        for j in range(agent_y/cube_scale):
            for p in range(agent_y/cube_scale):
                
                x0 = i
                y0 = j
                z0 = p
                
                r = i
                g = j
                b = p
                
                noStroke()
                fill(i,j,p)
                translate(x0,y0,z0)
                box(1)
                translate(-x0,-y0,-z0)
