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
    size(500,500)
    background(255)
    
    #setting the color mode and value scales. 
    colorMode(HSB,360,100,100)

def draw():

    #set the start and end colors in RGB and convert to processing color number
    

    #this moves the default processing origin to the center of the window
    translate(250,250)

    #saturation and brightness of the color
    sat_val = 100
    bri_val = 100
    
    for i in range(360):
        
        #establish the angle at the beginning of each loop and convert it to radians where pi*radian = 180 degrees
        angle = radians(i)
        print angle
        
        #calculate the endpoints of the line drawn in each loop
        x = cos(angle)*sat_val*2
        y = sin(angle)*sat_val*2
        
        #draw a new line with a new endpoint and color value each loop
        stroke(i,sat_val,bri_val)
        strokeCap(SQUARE)
        strokeWeight(5)
        line(0,0,x,y)
        
        print(i,sat_val,bri_val)
        print ("Still Looping!")
        
    print("Done")
    noLoop()
#*****************************************************************************
#End
