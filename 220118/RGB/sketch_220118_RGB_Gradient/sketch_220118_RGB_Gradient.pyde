#*****************************************************************************
#Woodbury University SoA
#CSMA 112 Spring 2022 Branda/Ericson
#
#Student Name: Mark Ericson
#Date: 01/18/22
#
#Project Name: Linear Gradient
#Project Description: This sketch creates a linear gradient from one edge of the window to the other. 
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

def draw():

    #set the start and end colors in RGB and convert to processing color number
    from_color = color(255,0,0)
    to_color   = color(0,0,255)


    for i in range(500):

        #establish color percentage each time the loop runs
        color_perc = float(i)/500.0
        
        #set the color value each time the loop runs
        color_val = lerpColor(from_color,to_color,color_perc)
        print color_val
        
        #assign a color value and create a line each time the loop runs where "i" defines the x cooridinate of each endpoint
        stroke(color_val)
        line(i,0,i,1000)
        print ("Still Looping!")
        
    print("Done")
    noLoop()
#*****************************************************************************
#End
