
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
    scale(1)
    
    #rotate initial view of cube

    rotateX(radians(45))
    rotateZ(radians(45))
    noFill()
    
    
    scale(20)
    
    #create loop that iterates through color values in a cylinder

    for H in range(360):
        #convert H to radians 
        angle = radians(H)
        for S in range(10):
            #get the x and y coordinates create S number of circles
            x = cos(angle)*S
            y = sin(angle)*S
            #get the V Values and stack the S number of circle V times
            for V in range(10):
                stroke(H,S,V)
                strokeWeight(2)
                point(x,y,V)

#*****************************************************************************
#End
