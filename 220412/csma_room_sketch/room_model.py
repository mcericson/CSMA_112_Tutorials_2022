
def set_color_mode():
    colorMode(HSB,360,10,10)
    background(0,0,100) 
      
def room_box(distance, pitch, roll):
    
    room_width =  300
    room_depth =  300
    room_height = 300
    
    rotateZ(radians(pitch))
    rotateY(radians(roll))
    
    h_value = abs(map(pitch, 0, 180, 0, 360))
    s_value = map(distance, 0, 24, 0 , 10)
    v_value = 10
    
    background(h_value/2, s_value/2, v_value)
    
    room_color = color(h_value, s_value, v_value)
    
    fill(room_color)
    noStroke()
    box(room_width, room_height, room_depth)
