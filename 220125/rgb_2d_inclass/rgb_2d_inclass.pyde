#settings

x_dim = 800
y_dim = 800

bg_color = x_dim

def setup():
    
    size(x_dim,y_dim)
    
    colorMode(RGB,x_dim)
    background(bg_color)
    
    
def draw():
    
    
    for i in range(x_dim):
        for j in range(y_dim):
            
            x0 = i
            y0 = j
            
            r = i
            g = j
            b = 0
            
            stroke(r,g,b)
            rect(x0,y0,1,1)
            
    noLoop()
