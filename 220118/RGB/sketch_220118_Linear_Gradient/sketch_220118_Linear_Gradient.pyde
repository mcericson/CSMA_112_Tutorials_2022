
#imports

from PointOnLine import PointOnLine
from Slider import Slider

#Global Variables
Width   = 1000
Height  = 1000
CenterX = Width/2
CenterY = Height/2




def setup():
    
    size(Width,Height,P3D)
    smooth(100)
    
def draw():
    global CenterX, CenterY
    
    background(250,240,240)
    
    #move origin to center of viewport
    translate(CenterX,CenterY)
    
    scale(.9)
    
    #rotate the viewport about the x axis
    rotateX(radians(45))
    
    #Angle on the horizontal plane of the line
    
    Angle = 0
    
    #scalar value by w+ s- on the keypad
    scalar = Slider()
    
    #starting point of the line
    x1,y1,z1 = 0,0,0
    
    #ending point of the line
    x2 = (cos(radians(Angle)))*255
    y2 = (sin(radians(Angle)))*255
    z2 = 255
    
    Point = PointOnLine(x1,y1,z1,x2,y2,z2,scalar)
    x3 = Point[0]
    y3 = Point[1]
    z3 = Point[2]
    

    

    stroke(255)
    line(x1,y1,z1,x2,y2,z2)
    line(x1,y1,z1,x2,y2,z1)
    line(x2,y2,z2,x2,y2,z1)
    
    fill(x3,y3,z3)
    ellipse(x1,y1,255*2,255*2)
    xval = int(x3)
    yval = int(y3)
    zval = int(z3)
    fill(100)
    textSize(20)
    text(str((0,0,0)),0,0,0)
    text(str((255,0,255)),x2,y2,z2)
    text(str((xval,yval,zval)),x3,y3,z3)
    translate(x3,y3,z3)
    sphere(5)
    
    
    
    print x3,y3,z3
    
    save("Linear.png")
