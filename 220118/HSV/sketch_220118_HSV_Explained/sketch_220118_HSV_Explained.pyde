
#*****************************************************************************
#Woodbury University SoA
#CSMA 112 Spring 2022 Branda/Ericson
#
#Student Name: Mark Ericson
#Date: 01/18/22
#
#Project Name: Linear Gradient
#Project Description: This sketch explains the RGB cube.
#*****************************************************************************
#External Sources and Referencess//Provide full web address

#Source:  https://py.processing.org/reference/
#Source:  https://google.github.io/styleguide/pyguide.html#s3.16.2-naming-conventions
#source:  https://py.processing.org/reference/colorMode.html
#source: https://www.mrfeinberg.com/peasycam/
#
#*****************************************************************************
#imported Libraries
#

add_library('peasycam')
import math
import os
from orientedText import orientedText

#
#*****************************************************************************
#Functions:



#*****************************************************************************
#Project Settings



#*****************************************************************************
#Main Program

def setup():
    global edge_number
    size(1000,1000,P3D)
    #move processing origin to center of the sheet

    translate(500,500)
    #place the camera 1000 pixels from the origin
    cam = PeasyCam(this,1000)
    
    #set the minumum camera distance 
    cam.setMinimumDistance(0)
    #set the maximum camera distance 
    cam.setMaximumDistance(1000)
    
    #set background orthographic projection
    ortho()
    #setting the color mode and value scales.
    #setting the edge_number to 255 would match the cube to the color system, but it is also very slow to render.

    colorMode(HSB,360,10,10)
    

def draw():

    background(355,.6,10)
    
    #scale up cube and pixels         

    
    #rotate initial view of cube
    rotateX(radians(-60))
    rotateZ(radians(45))
    noFill()
    
    shapeMode(CENTER)
    stroke(360,0,10)
    strokeWeight(3)
    
    #create cylinder 
    circle(0,0,400)

    for i in range(0,360,60):
        angle = radians(i)
        x = cos(angle)*200
        y = sin(angle)*200
        line(x,y,0,x,y,200)

    x1 = cos(radians(360))*200
    y1 = sin(radians(360))*200
    
    x2 = cos(radians(300))*200
    y2 = sin(radians(300))*200
    
    x3 = cos(radians(360))*100
    y3 = sin(radians(360))*100
    
    pushMatrix()
    translate(0,0,200)
    circle(0,0,400)
    popMatrix()
    
    #draw illustration lines for HSB values

    line(x1,y1,200,0,0,200)
    line(x2,y2,200,0,0,200)
    line(x1,y1,0,0,0,0)
    line(x2,y2,0,0,0,0)
    line(0,0,0,0,0,200)
    line(x1,y1,0,0,0,0)

    #label HSB values
    
    text_color = color(300,10,10)
    
    stroke(text_color)
    strokeWeight(50)
    arc(x1,y1,10,10,radians(60),radians(0))
    
    orientedText ("Saturation",0,0,0,"Arial",30,text_color)

    orientedText ("Hue",x1,y1,270,"Arial",30,text_color)
    
    translate(0,0,200)
    rotateY(radians(90))
    orientedText ("Brightness",0,0,0,"Arial",30,text_color)







    



    save("HSV_expl.png")

    

#*****************************************************************************
#End
