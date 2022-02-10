add_library('sound')
import rgb_model as model
import microphone 
from agent import Agent
import samples

agent = Agent()
agent.set_history_enabled(True)
samples.buffer_size = 6


def setup():
    size(model.x_dim, model.y_dim)
    model.set_color_mode() #changed to set color mode in module
    microphone.initialize(this, AudioIn, Amplitude)
    microphone.sensitivity = 4.0
    frameRate(20)


def draw():
    sound_level = microphone.get_level()
    samples.add_sample(sound_level)
    agent_param_0 = samples.get_smoothed()
    agent_param_1 = 0.5
    x, y = model.get_agent_location(agent_param_0, agent_param_1)
    agent.move_to(x, y)
    render()


def render():
    noStroke()
    background(model.get_white())
    agent_color = model.get_agent_location_color(agent.x, agent.y)
    fill(agent_color)
    rect(agent.x, agent.y, 20, 20)
    for hx, hy in agent.history:
        agent_color = model.get_agent_location_color(hx, hy)
        fill(agent_color)
        rect(hx, hy, 20, 20)
        
        
    



    
