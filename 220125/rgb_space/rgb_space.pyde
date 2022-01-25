
import rgb_3d as model

def setup():
    
    size(model.x_dim, model.y_dim,model.render)
    colorMode(model.color_mode,model.color_dim)
    background(model.bg_color)
    ortho()


    
def draw():
    
    model.rot_deg += mouseY/(mouseX+.0001)
    
    model.agent_x = mouseX
    model.agent_y = mouseY
    
    background(model.agent_x,model.agent_y,model.agent_x/2)
    model.rgb_model()
    
