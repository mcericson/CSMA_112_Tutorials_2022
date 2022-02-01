x_dim = 800
y_dim = 800
scale_val = 10
h_val = 360
s_val = 20
v_val = 10

def setup():
    
    size(x_dim,y_dim,P3D)
    colorMode(HSB,h_val,s_val,v_val)
    
def draw():
    
    background(h_val*.9,s_val*.06,v_val,)
    translate(x_dim/2,y_dim/2)
    ortho()
    
    rot_angle = radians(frameCount)
    rotateX(rot_angle)
    scale(scale_val)
    noStroke()
    for i in range(h_val):
        angle = radians(i)
        for j in range(s_val):
            x = cos(angle)*j
            y = sin(angle)*j
            for p in range(v_val):

                z = p
            
                h = i
                s = j
                v = p
            
                stroke(h,s,v)
                point(x,y,z)
