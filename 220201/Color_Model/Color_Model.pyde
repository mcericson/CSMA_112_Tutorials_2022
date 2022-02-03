add_library('sound')
import rgb_model as model


import microphone 

def setup():
    size(model.x_dim,model.y_dim)
    color_val_1, color_val_2, color_val_3 = model.color_max_value
    colorMode(model.color_mode,color_val_1, color_val_2, color_val_3)
    microphone.initialize(this, AudioIn, Amplitude)
    microphone.sensitivity = 3.0
    frameRate(2)
    
def draw():
    sound_level = microphone.get_level()

    agent_x = sound_level 
    agent_y = 0.5 
    
    
    
    model.current_h_val = 360*sound_level
    
    
    model.update_agent_location(agent_x,agent_y)
    color_1, color_2, color_3 = model.get_current_color_values()
    print(color_1, color_2, color_3)
    background(color_1, color_2, color_3)
    print(model.current_h_val)
    x,y = model.agent_x, model.agent_y

    strokeWeight(2)
    line(x-10,y,x+10,y)
    line(x,y-10,x,y+10)
