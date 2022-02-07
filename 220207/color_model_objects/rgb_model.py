
import time

class RGB_Model(object):
    
    def __init__(self):


        self.x_dim = 500
        self.y_dim = 500
        self.color_mode = RGB
        self.color_max_value = self.x_dim
        
        self.location = []
        self.color_val = []
        self.birthday = int(time.time()*1000)
        self.lifespan = 3000
        
        self.agent_x = 0.0
        self.agent_y = 0.0
        
    def set_color_mode(self):
        colorMode(self.color_mode, self.color_max_value)
        
    def update_agent_age(self):
        
        now = int(time.time()*1000)
        self.agent_age =  now - self.birthday
        
        return self.agent_age
    
    def update_agent_location(self,x_norm,y_norm, z_norm=0.0):

        self.agent_x = x_norm * self.x_dim
        self.agent_y = mouseY
        
        
    def get_agent_location_color(self):
        
        r = self.agent_x * (self.color_max_value/self.x_dim)
        g = self.agent_y * (self.color_max_value/self.y_dim)
        b = 0
        
        color_value =  color(r, g, b)
        self.color_val.append(color_value)
        
        if len(self.color_val) > 500:
            self.color_val.pop(0)
        
        return(self.color_val)
        
    
    def get_agent_location(self):
        
        self.location.append((self.agent_x,self.agent_y))
        
        if len(self.location) > 500:
            self.location.pop(0)
        return self.location
        
    def get_white(self):
        
        return color(self.color_max_value)
