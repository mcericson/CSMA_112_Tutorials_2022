add_library('sound')
from hsv_model import HSV
import microphone 


model = HSV()
def setup():
    global  model
    
    
    size(model.x_dim,model.y_dim)
    model.set_color_mode() #changed to set color mode in module
    microphone.initialize(this, AudioIn, Amplitude)
    microphone.sensitivity = 5.0
    frameRate(20)
    

    
def draw():
    sound_level = microphone.get_level()

    agent_param_0 = sound_level #rgb is agent_x//hsv is angent_agle
    agent_param_1 = 0.5 #rgb is agent_y//hsv is agent_radius
    model.update_agent_location(agent_param_0, agent_param_1)
    render()
    
def render():
    noStroke()
    
    color_vals = model.get_agent_location_color()
    agent_locations = model.get_agent_location()
    for i in range(len(color_vals)):
        if len(color_vals) > 1:
            background(color_vals[i-1])

    #background(model.get_white())
    for i in range(len(color_vals)):
        fill(color_vals[i])
        x0,y0 = agent_locations[i]
        rect(x0,y0,10,10)




    
