import rgb_model as model # Run the code in the file "model.py"

def setup():
    size(model.x_dim, model.y_dim)
    colorMode(model.color_mode, model.x_dim)


def draw():
    
    # Update the agent in its environment
    model.agent_x = mouseX
    model.agent_y = mouseY
    
    # Render new "view"
    r, g, b = model.get_agent_color()
    fill(r, g, b)
    background(model.bg_color)
    circle(model.agent_x, model.agent_y, model.flashlight_diameter) 
    
