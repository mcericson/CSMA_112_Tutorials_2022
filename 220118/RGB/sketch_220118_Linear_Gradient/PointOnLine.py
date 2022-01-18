#This function locates a point on a line with its two endpoints and a scalar
#mark ericson 1.27.21

def PointOnLine(x1,y1,z1,x2,y2,z2,scalar):
    
    #finds point on a line
    x3 = float((x1 + x2)*scalar)
    y3 = float((y1 + y2)*scalar)
    z3 = float((z1 + z2)*scalar)
    
    #Constrain the result by the endpoints
    
    if (x3,y3,z3) >= (x2,y2,z2):
        
        x3,y3,z3 = x2,y2,z2
    
    if (x3,y3,z3) <= (x1,y1,z1):
        
        x3,y3,z3 = x1,y1,z1
    
    return(x3,y3,z3)
