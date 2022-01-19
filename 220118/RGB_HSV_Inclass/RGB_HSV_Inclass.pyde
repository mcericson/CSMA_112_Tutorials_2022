size(800,800)
colorMode(HSB,800,100,100)

#This sets the background color of the window
background(800)

#This program will drawn n number of vertical lines to create a color gradient.

for i in range(800):
    x0 = i
    y0 = 0
    x1 = i
    y1 = 800
    H = i
    S = 100
    V = 100
    stroke(H,S,V)
    line(x0,y0,x1,y1)
    
