add_library('pdf')
add_library('sound')

import hsv_model as model
import microphone 
import output_tools as output
from recorder import Recorder
import os

stop_point = 500

file_name = os.path.basename(__file__)

def setup():
    global agent_record, stop_point, file_name, calibri_font
    size(model.x_dim,model.y_dim)
    model.set_color_mode() #changed to set color mode in module
    microphone.initialize(this, AudioIn, Amplitude)
    microphone.sensitivity = 3.0
    frameRate(20)
    
    pixelDensity(2)
    
    agent_record = Recorder()
    
    calibri_font = createFont("calibri",15)
    
    output.save_pdf(False,file_name)
    
def draw():
    output.save_raw(False,file_name)
    sound_level = microphone.get_level()

    agent_param_0 = sound_level #rgb is agent_x//hsv is angent_agle
    agent_param_1 = 0.5 #rgb is agent_y//hsv is agent_radius
    model.update_agent_location(agent_param_0, agent_param_1)
    render()
    
    output.save_movie(False)
    
    if frameCount == stop_point:
        noLoop()
        output.save_image(False, file_name)
        endRaw()
        endRecord()
        print ("Done")
    
def render():
    noStroke()
    background(model.get_white())
    
    color_val = model.get_agent_location_color()
    color_vals = agent_record.get_recorded_color(color_val)

    x,y = model.get_agent_location()  
    agent_locations = agent_record.get_recorded_location(x,y)  
    
    for i in range(len(color_vals)):
        
        background(color_vals[i-1])
    
    for i in range(len(color_vals)):
        fill(color_vals[i])
        x0,y0 = agent_locations[i]
        rect(x0, y0, 20 ,20)
        
    textFont(calibri_font)
    label = model.get_color_values()
    fill(model.get_white())
    text(str(label), x, y)    
    



    
