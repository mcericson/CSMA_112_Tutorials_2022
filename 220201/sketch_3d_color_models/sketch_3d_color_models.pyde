add_library('sound')
import rgb_model as model


import microphone 

def setup():
    size(model.x_dim,model.y_dim,model.render)
    

    colorMode(model.color_mode,model.a_val, model.b_val, model.c_val)
    microphone.initialize(this, AudioIn, Amplitude)
    microphone.sensitivity = 20.0
    frameRate(20)
    
def draw():

    sound_level = microphone.get_level()

    agent_x = sound_level 
    agent_y = 0.5 
    
    model.update_agent_location(agent_x,agent_y)
    r, g, b = model.get_current_rgb_values()
    
    x,y = model.agent_x, model.agent_y
    model.hsv_cylinder(x,y,sound_level)

    stroke(0)
    strokeWeight(2)
    
    
    line(x-10,y,x+10,y)
    line(x,y-10,x,y+10)
    
    
