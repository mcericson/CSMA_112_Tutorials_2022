#*****************************************************************************
#Woodbury University SoA
#CSMA 112 Spring 2022 Branda/Ericson
#
#Student Name: Mark Ericson
#Date: 01/18/22
#
#Project Name: Linear Gradient
#Project Description: This sketch colors every point(pixel) in the window with a HSV color value to create gradient.
#
#*****************************************************************************
#External Sources and Referencess//Provide full web address

#Source:  https://py.processing.org/reference/
#Source:  https://google.github.io/styleguide/pyguide.html#s3.16.2-naming-conventions
#source:  https://py.processing.org/reference/colorMode.html
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
    colorMode(HSB,500)

def draw():

    noStroke()
    for Red in range(1000):
        for Green in range(1000):
            stroke(Red,Green,1000)
            point(Red,Green)
        
    
    save("HSV_Gradient.png")
        
    print("Done")
    noLoop()
#*****************************************************************************
#End
