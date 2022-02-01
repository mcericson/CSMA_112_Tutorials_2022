add_library('sound')
import rgb_model as model


import microphone 

def setup():
    size(model.x_dim,model.y_dim)
    colorMode(model.color_mode,model.color_max_value)
    microphone.initialize(this, AudioIn, Amplitude)
    microphone.sensitivity = 3.0
    frameRate(2)
    
def draw():
    sound_level = microphone.get_level()

    agent_x = sound_level 
    agent_y = 0.5 
    
    model.update_agent_location(agent_x,agent_y)
    r, g, b = model.get_current_rgb_values()
    
    background(r,g,b)
    stroke(model.color_max_value)
    strokeWeight(2)
    x,y = model.agent_x, model.agent_y
    
    line(x-10,y,x+10,y)
    line(x,y-10,x,y+10)
