def set_color_mode():
    colorMode(HSB, 360, 10, 10)
    background(0,0,10)
    

def room_box(distance, pitch, roll):
    print distance, pitch, roll
    room_width = width/3
    room_depth = width/3
    room_height = width/3
    
    rotateZ(radians(pitch))
    rotateY(radians(roll))
    
    h_value = map(pitch, 0, 180, 0, 360)
    s_value = map(distance, 0, 6, 0, 10)
    v_value = 10
    
    room_color = color(h_value, s_value, v_value)
    print s_value
    
    fill(room_color)
    noStroke()
    box(room_width, room_height, room_depth)
