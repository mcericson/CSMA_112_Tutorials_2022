add_library('sound')
#settings

x_dim = 800
y_dim = 800

cube_dim = 20

bg_color = cube_dim



def setup():
    global amp
    mic = AudioIn(this,0)
    mic.start()
    amp = Amplitude(this)
    
    amp.input(mic)
    size(x_dim,y_dim,P3D)
    
    colorMode(RGB,cube_dim)
    background(bg_color)
    ortho()
    
    
def draw():
    background(mouseX,mouseY)
    translate(x_dim/2, y_dim/2)
    scale(10)
    strokeCap(SQUARE)
    
    sound_level = amp.analyze()
    print sound_level
    rot_deg = radians(frameCount + 90*sound_level)
    
    rotateX(rot_deg)
    rotateY(rot_deg)
    
    
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
                
                
