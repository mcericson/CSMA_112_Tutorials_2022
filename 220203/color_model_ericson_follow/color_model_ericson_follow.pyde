add_library('sound')
import rgb_model as model
import microphone 

def setup():
    size(model.x_dim,model.y_dim)
    model.set_color_mode()
    microphone.initialize(this, AudioIn, Amplitude)
    microphone.sensitivity = 3.0
    frameRate(20)
    
def draw():
    sound_level = microphone.get_level()
    agent_param_0 = sound_level 
    agent_param_1 = 0.5 
    model.update_agent_location(agent_param_0,agent_param_1)
    render()
 
def render():
    background(model.get_agent_location_color())
    stroke(model.get_white())
    strokeWeight(2)
    x,y = model.get_agent_location_xy()
    line(x-10,y,x+10,y)
    line(x,y-10,x,y+10)
