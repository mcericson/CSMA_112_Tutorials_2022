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
    x = mouseX
    y = mouseY
    agent = [x,y,now()]
    history.append(agent)
    
    if len(history) > 500:
        history.pop(0)
    
    for agent in history:
        #compute the location and color for agent
        x, y = agent[0], agent[1]
        r, g , b  = x, y, 0
        
        #compute the transparency  based on agent's age
        age = now() - agent[2] 
        fade_factor = age / float(life_span)
        a = 100 - fade_factor * 100
        
        #render
        fill(r,g,b, a)
        circle(x, y, 20)
        
    print(agent)
    
    
    
    
def now():
    return int(time.time() * 1000)
    
    
