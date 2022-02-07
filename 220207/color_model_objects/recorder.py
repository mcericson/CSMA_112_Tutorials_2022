
import time

class Recorder(object):
    
    def __init__(self):
        
    
        self.location  = []
        self.color_val = []
        self.birthday = int(time.time()*1000)
        self.age = []

            
    def get_recorded_location(self,x,y):
        
        self.location.append((x,y))
        
        if len(self.location) > 500:
            
            self.location.pop(0)
        
        print(self.location)
        
        return(self.location)
        
    def get_recorded_color(self,color_value):
        
        self.color_val.append(color_value)
    
        if len(self.color_val) > 500:
            
            self.color_val.pop(0)
        
        return(self.color_val)
    

        
        
        
