value = 0

def Slider():
    
    global value
    
    if keyPressed:
        
        if key == 'w':
            
            value += .01
        
        if key == 's':
            
            value -= .01
            
        return(value)
    
    if not keyPressed:
        
        value = value
        
        return(value)
