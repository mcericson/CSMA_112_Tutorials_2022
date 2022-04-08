
import server


listener = None
    
    
def setup():
    size(400, 400)
    global listener
    listener = server.Connection(this, 8080)
    

def draw():
    msg = listener.get_message()
    if msg:
        process_input(msg)


def process_input(msg):
    value = msg.get_value("dist")
    if value:
        try:
            rgb_val = int(value)
            print(rgb_val)
            background(rgb_val)
        except:
            pass


def setup_test():
    size(400, 400)
    process_input(server.Message("dist=0"))