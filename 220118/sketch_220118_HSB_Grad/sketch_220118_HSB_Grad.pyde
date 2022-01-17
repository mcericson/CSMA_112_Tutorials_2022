#*****************************************************************************
#Woodbury University SoA
#CSMA 112 Spring 2022 Branda/Ericson
#
#Student Name: Mark Ericson
#Date: 01/18/22
#
#Project Name: Linear Gradient
#Project Description: This sketch creates a circular gradient using the HSV (HSB) color system
#
#*****************************************************************************
#External Sources and Referencess//Provide full web address

#Source:  https://py.processing.org/reference/
#Source:  https://google.github.io/styleguide/pyguide.html#s3.16.2-naming-conventions
#source:
#
#*****************************************************************************
#imported Libraries
#

import math
import os

#
#*****************************************************************************
#Functions:



#*****************************************************************************
#Project Settings

Color = (255,255,255)

#*****************************************************************************
#Main Program

def setup():
    size(1000,1000)
    background(255)
    
    #setting the color mode and value scales. 
    colorMode(HSB,360,100,100)

def draw():

    #set the start and end colors in RGB and convert to processing color number
    

    #move the default processing origin to the center of the window
    translate(500,500)
    
    #scale the drawing up 
    scale(4)
    

    for H in range(360):
        angle = radians(H)
        for S in range(100):
            x = cos(angle)*S
            y = sin(angle)*S
            stroke(H,S,100)
            strokeWeight(2)
            point(x,y)
        
        

        
    print("Done")
    noLoop()
#*****************************************************************************
#End
