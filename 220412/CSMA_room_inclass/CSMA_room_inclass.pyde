
import server
import room_model as model



listener = None
    
    
def setup():
    size(1000,1000,P3D)
    global listener
    listener = server.Connection(this, 8080)
    model.set_color_mode()
    frameRate(5)

def draw():
    translate(width/2, height/2)
    msg = listener.get_message()
    render_message(msg)



def process_input(value, default):
    new_value = default
    value = msg.get_value("dist")
    if value:
        try:
            new_value = float(value)
        except:
            pass
    return new_value

def render_message(msg):
    
    default_dist = 24
    default_pitch = 90
    default_roll = 90
    
    if msg:
        msg_1 = msg.get_value("dist")
        msg_2 = msg.get_value("pitch")
        msg_3 = msg.get_value("roll")
        
        dist_val = process_input(msg_1, default_dist)
        pitch_val = process_input(msg_2, default_pitch)
        roll_val = process_input(msg_3, default_roll)
        
        model.room_box(dist_val, pitch_val, roll_val)
    else:
        model.room_box(default_dist, default_pitch, default_roll)




def setup_test():
    size(400, 400)
    process_input(server.Message("dist=0"))
