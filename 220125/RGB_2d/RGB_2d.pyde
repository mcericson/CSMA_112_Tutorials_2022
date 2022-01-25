x_dim = 
y_dim = 
bg = 255

def setup():
    
    size(x_dim,y_dim)
    background(255)
    
    colorMode(RGB, x_dim)
    
    
def draw():
    

    
    for i in range(x_dim):
        for j in range(y_dim):
            x0 = i
            y0 = j
            
            r = i
            g = j
            b = 0
            
            stroke(r,g,b)
            point(x0,y0)
            
    noLoop()
