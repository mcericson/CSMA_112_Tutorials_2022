add_library('sound')
from hsv_model import HSV_Model
from rgb_model import RGB_Model
import microphone 


#set model type here RGB_Model or HSV_Model
model = RGB_Model()

def setup():
    global  model

    size(model.x_dim,model.y_dim)
    model.set_color_mode() #changed to set color mode in module
    microphone.initialize(this, AudioIn, Amplitude)
    microphone.sensitivity = 10.0
    frameRate(20)
    

    
def draw():
    sound_level = microphone.get_level()

    agent_param_0 = sound_level #rgb is agent_x//hsv is angent_agle
    agent_param_1 = 1.0 #rgb is agent_y//hsv is agent_radius
    model.update_agent_location(agent_param_0, agent_param_1)
    render()
    
def render():
    noStroke()
    
    color_vals = model.get_agent_location_color()
    agent_locations = model.get_agent_location()
    
    
    for i in range(len(color_vals)):
        if len(color_vals) > 1:
            background(color_vals[i-1])

    for i in range(len(color_vals)):
        fill(color_vals[i])
        x0,y0 = agent_locations[i]
        rect(x0,y0,20,20)





    
