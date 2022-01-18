
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
    colorMode(HSB,360,100,10)
    

def draw():

    background(355,6,100)
    translate(500,500)
    #scale up cube and pixels         
    scale(2)
    
    #rotate initial view of cube


    noFill()

    scale(2)
    
    #create loop that iterates through color values in a cylinder

    for H in range(360):
        #convert H to radians 
        angle = radians(H)
        for S in range(100):
            #get the x and y coordinates create S number of circles
            x = cos(angle)*S
            y = sin(angle)*S
            
            stroke(H,S,100)
            strokeWeight(2)
            point(x,y,0)
            
    save("HSV_2d.png")
    noLoop()

#*****************************************************************************
#End
