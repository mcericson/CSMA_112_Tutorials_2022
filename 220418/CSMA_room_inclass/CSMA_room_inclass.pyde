
import server
import room_model as model


listener = None
    
    
def setup():
    size(1000,1000,P3D)
    model.set_color_mode()
    frameRate(30)
    ortho()
    global listener
    listener = server.Connection(this, 8080)


def draw():
    
    msgs = listener.get_messages()
    if not msgs: return
    
    # Defaults
    dist_val =  24
    pitch_val = 90
    roll_val =  90
    
    for msg in msgs:
        if not msg.value_is_numeric(): continue
        if msg.has_key("dist"):
            dist_val = msg.get_value()
        elif msg.has_key("pitch"):
            pitch_val = msg.get_value()
        elif msg.has_key("roll"):
            roll_val = msg.get_value()

    print([m.to_str() for m in msgs]) # Print the messages received for debugging
    add_x = map(pitch_val, 0, 90, 0,width/4)
    add_y = map(roll_val, 0, 90, 0,width/4) 
    translate((width/2) + add_x, (height/2) + add_y)
    model.room_box(dist_val, pitch_val, roll_val)
