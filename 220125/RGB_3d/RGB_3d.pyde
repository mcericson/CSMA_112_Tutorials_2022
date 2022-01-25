x_dim = 800
y_dim = 800

cube_dim = 20
bg = 255


def setup():
    
    size(x_dim,y_dim,P3D)
    background(cube_dim)
    
    colorMode(RGB, cube_dim)
    
    
def draw():
    strokeCap(SQUARE)
    strokeWeight(2)
    background(cube_dim)
    
    rot_deg = radians(frameCount)
    translate(x_dim/2,y_dim/2)
    
    rotateX(rot_deg)
    rotateZ(rot_deg)
    rotateY(rot_deg)
    
    scale(10)
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
            
