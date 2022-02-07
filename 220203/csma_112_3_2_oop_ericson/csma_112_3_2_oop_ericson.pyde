import time


history = []
life_span = 3000

def setup():
    
    size(500,500)
    frameRate(20)
    colorMode(RGB,width, height, 255, 100)
    noStroke()
    
def draw():
    background(0)
    agent = Agent()
    agent.move_to(mouseX, mouseY)
    history.append(agent)
    
    if len(history) > 500:
        history.pop(0)
    
    for agent in history:
        #compute the location and color for agent
        
        r, g , b  = agent.x, agent.y, 0
        
        #compute the transparency  based on agent's age
        age = agent.get_age 
        fade_factor = agent.get_age() / float(agent.life_span)
        a = 100 - fade_factor * 100
        
        #render
        fill(r,g,b, a)
        circle(agent.x, agent.y, agent.radius)
        

def now():
    return int(time.time() * 1000)
    
            
class Agent(object):
    #location x,y
    #age
    #lifespan
    
    def __init__(self):
        
        self.x = 0
        self.y = 0
        self.life_span = 3000
        self.birthday = now()
        self.radius = 20
    
    def move_to(self, x, y):
        
        self.x = x
        self.y = y
    
    def get_age(self):
        return now()  - self.birthday

    
my_agent = Agent()

print(my_agent.get_age())    
    

    
    
