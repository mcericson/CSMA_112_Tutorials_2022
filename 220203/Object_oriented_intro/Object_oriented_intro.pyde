import time

history = []

def setup():
    size(500,500)
    frameRate(20)
    colorMode(RGB, width, height, 255, 100)
    noStroke()
    

def draw():
    
    # Update the list of agents
    agent = Agent()
    agent.move_to(mouseX, mouseY)
    history.append(agent)
    # Make sure that the history never exceeds 500 agents
    if len(history) > 500:
        history.pop(0)
        
    # Render the list of agents
    background(0)
    for agent in history:
        r, g, b = agent.x, agent.y, 0
        fade_factor = agent.get_age() / float(agent.lifespan)
        a = 100 - fade_factor * 100 # Remember order of operations?
        fill(r, g, b, a)
        circle(agent.x, agent.y, agent.radius)


def now():
    return int(time.time() * 1000)


class Agent(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.lifespan = 3000
        self.birthday = now()
        self.radius = 20
        
    def move_to(self, x, y):
        self.x = x
        self.y = y
    
    def get_age(self):
        return now() - self.birthday
