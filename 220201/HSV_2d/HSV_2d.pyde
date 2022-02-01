x_dim = 800
y_dim = 800
scale_val = 2
h_val = 360
s_val = 100
v_val = 10

def setup():
    
    size(x_dim,y_dim,P2D)
    colorMode(HSB,h_val,s_val,v_val)
    
def draw():
    
    background(h_val*.9,s_val*.06,v_val,)
    translate(x_dim/2,y_dim/2)
    scale(scale_val)
    noStroke()
    for i in range(h_val):
        angle = radians(i)
        for j in range(s_val):
            x = cos(angle)*j
            y = sin(angle)*j
            
            h = i
            s = j
            v = v_val
            
            stroke(h,s,v)
            strokeWeight(2)
            point(x,y,0)
    noLoop()     
