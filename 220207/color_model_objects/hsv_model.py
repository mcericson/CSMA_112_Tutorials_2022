import time

class HSV(object):

    def __init__(self):
    
        self.x_dim = 500
        self.y_dim = 500
        self.color_mode = HSB
        self.radius_max = self.x_dim/3
        self.v_val = 100
        self.angle_deg = 0.0
        self.radius = 0.0
        
        self.location  = []
        self.color_val = []
        self.birthday = int(time.time()*1000)
        self.lifespan = 3000
    
    def set_color_mode(self):
        #colorMode() = processing environment only
        colorMode(self.color_mode, 360, self.radius_max, self.v_val)
    
    def update_agent_age(self):
        
        now = int(time.time()*1000)
        self.agent_age =  now - self.birthday
        
        return self.agent_age
        
    
    def update_agent_location(self,angle_norm,radius_norm):
    
        self.angle_deg = angle_norm*360
        self.radius = radius_norm * self.radius_max
        
    def get_agent_location(self):
        
        agent_x = self.x_dim/2 + cos(radians(self.angle_deg)) * self.radius
        agent_y = self.y_dim/2 + sin(radians(self.angle_deg)) * self.radius
        
        self.location.append((agent_x,agent_y))
        
        if len(self.location) > 500:
            self.location.pop(0)
        
        return self.location
    
    def get_agent_location_color(self):
        
        h = self.angle_deg
        s = self.radius
        v = self.v_val
        
        fade_factor = self.update_agent_age() / float(self.lifespan)

        #color()  = processing environment only
        color_value = color(h, s, v)
        self.color_val.append(color_value)
        
        if len(self.color_val) > 500:
            self.color_val.pop(0)
        
        return(self.color_val)
        

    def get_white(self):
        
        #color()  = processing environment only
        return color(0, 0, 100)
