
from agent import Agent


agents = []

num_agents = 100
fps = 20
ppf = 5


def setup():
    size(500,500) # Set the size of the canvas
    frameRate(fps) # Set the sketch animation frame rate 
    
    # Build the list of agents
    for i in range(num_agents):
        agent = Agent()
        agent.direction = [random(0, 1), random(0, 1)]
        agents.append(agent)
    


def draw():
    background(255)
    for agent in agents:
        dx = ppf * agent.direction[0]
        dy = ppf * agent.direction[1]
        agent.move(dx, dy)
        agent.check_boundary(width, height)
        fill(100)
        circle(agent.x, agent.y, 50)
