def set_color_mode():
    colorMode(HSB, 360, 10, 10)
    background(0,0,10)
    

def room_box(distance, pitch, roll):
    room_width = width/3
    room_depth = width/3
    room_height = width/3
    

    
    h_value = map(distance, 0, 30, 0, 180)
    s_value = map(pitch, 0, 6, 0, 10)
    v_value = 10
    
    rotateZ(radians(pitch))
    rotateY(radians(roll))
    
    background(h_value/2, s_value/2, v_value)
    room_color = color(h_value, s_value, v_value)

    fill(room_color)
    stroke(0,0,10)
    box(room_width, room_height, room_depth)
