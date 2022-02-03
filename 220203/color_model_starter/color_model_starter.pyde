add_library('sound')
import rgb_model as model


import microphone 

def setup():
    size(model.x_dim,model.y_dim)
    colorMode(model.color_mode,model.color_max_value)
    microphone.initialize(this, AudioIn, Amplitude)
    microphone.sensitivity = 3.0
    frameRate(20)
    
def draw():
    sound_level = microphone.get_level()

    agent_x = sound_level 
    agent_y = 0.5 
    model.update_agent_location(agent_x,agent_y)
    render()
 
def render():
    color_1, color_2, color_3 = model.get_current_color_values()
    background(color_1, color_2, color_3)
    stroke(0,0,0)
    strokeWeight(2)
    x,y = model.agent_x, model.agent_y
    
    line(x-10,y,x+10,y)
    line(x,y-10,x,y+10)
