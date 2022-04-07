
def setup():
    
    size(500,500, P3D)
    background(255)
    ortho()
    
def draw():
    
    room_rotation = 45
    
    room_width = 200
    room_depth = 300
    room_height = 20
    
    translate(width/2, height/2)
    
    rotateX(radians(room_rotation))
    rotateY(radians(room_rotation))
    
    noFill()
    box(room_width, room_height, room_depth)
