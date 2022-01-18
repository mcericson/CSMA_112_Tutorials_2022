
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
    edge_number = 50
    colorMode(RGB,edge_number)
    

def draw():

    background(49,46,46)
    
    #scale up cube and pixels         

    
    #rotate initial view of cube
    rotateX(radians(45))
    rotateZ(radians(45))
    noFill()
    
    shapeMode(CENTER)
    stroke(50)
    strokeWeight(3)
    box(400)
    
    
    #notations of color cube cooridinates to correspond to RGB scale
    scale(1.04)
    textAlign(CENTER)
    textSize(30)
    #white
    fill(50)
    text("255,255,255",200,200,200)
    #black
    fill(0)
    text("0,0,0",-200,-200,-200)
    #red
    fill(50,0,0)
    text("255,0,0",200,-200,-200)
    #green
    fill(0,50,0)
    text("0,255,0",-200,200,-200)
    #blue
    fill(0,0,50)
    text("0,0,255",-200,-200,200)
    #yellow
    fill(50,50,0)
    text("255,255,0",200,200,-200)
    #Cyan
    fill(0,50,50)
    text("0,255,255",-200,200,200)
    #magenta
    fill(50,0,50)
    text("255,255,0",200,-200,200)
    




    

#*****************************************************************************
#End
