
x_dim = 1000
y_dim = 1000

color_min = 0
count = 0

def setup():
    background(255)
    frameRate(60)
    size(x_dim,y_dim)

def draw():
    global count, color_min
    count += 1
    
    distance = random(0,1000) #TODO replace with input from sensor
    x = count
    y = distance
    r = map(count, 0, x_dim, color_min,255)
    b = map(distance, 0, y_dim, color_min, 255)
    
    stroke(r,0,b)
    line(x, 0,x, y)
    
    if count == x_dim:
        background(255)
        count = 0
    
    
    
    
    
    
