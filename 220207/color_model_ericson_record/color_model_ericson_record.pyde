add_library('sound')
import hsv_model as model
import microphone 
from recorder import Recorder

def setup():
    global agent_record
    size(model.x_dim,model.y_dim)
    model.set_color_mode() #changed to set color mode in module
    microphone.initialize(this, AudioIn, Amplitude)
    microphone.sensitivity = 5.0
    frameRate(20)
    
    agent_record = Recorder()
    
def draw():
    sound_level = microphone.get_level()

    agent_param_0 = sound_level #rgb is agent_x//hsv is angent_agle
    agent_param_1 = 0.5 #rgb is agent_y//hsv is agent_radius
    model.update_agent_location(agent_param_0, agent_param_1)
    render()
    
def render():
    noStroke()
    color_val = model.get_agent_location_color()
    color_vals = agent_record.get_recorded_color(color_val)
    
    x,y = model.get_agent_location()
    agent_locations = agent_record.get_recorded_location(x,y)
    
    
    background(model.get_white())
    for i in range(len(color_vals)):
        fill(color_vals[i])
        x0,y0 = agent_locations[i]
        rect(x0,y0,10,10)




    
