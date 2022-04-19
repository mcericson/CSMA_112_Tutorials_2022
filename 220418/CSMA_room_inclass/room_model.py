def set_color_mode():
    colorMode(HSB, 360, 10, 10)
    background(0,0,10)
    smooth(1000)
    

def room_box(distance, pitch, roll):

    

    
    h_value = map(distance, 0, 30, 0, 180)
    s_value = map(pitch, 0, 6, 0, 10)
    v_value = 10
    
    room_width = map(distance, 0, 30, 1, width/3)
    room_depth = map(pitch, 0, 6, 1, width/3)
    room_height = map(roll, 0, 6, 1, width/3)
    
    scale_val = map(distance, 0, 30, 0, 2)
    rotateZ(radians(abs(pitch)))
    rotateY(radians(abs(roll)))
    
    background(h_value/2, s_value/2, v_value)
    room_color = color(h_value, s_value, v_value)

    fill(room_color)
    stroke(0,0,0)
    scale(scale_val)
    box(room_width, room_height, room_depth)
