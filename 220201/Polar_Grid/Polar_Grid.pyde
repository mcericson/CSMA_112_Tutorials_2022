x_dim = 800
y_dim = 800

def setup():
    
    size(x_dim,y_dim,P2D)
    

def draw():
    
    translate(x_dim/2,y_dim/2)
    
    scale(100)

    for i in range(360):
        angle = radians(i)
        for j in range(4):
            radius = j
            x = cos(angle)*radius
            y = sin(angle)*radius
            
            noFill()
            strokeWeight(.02)
            point(x,y)
