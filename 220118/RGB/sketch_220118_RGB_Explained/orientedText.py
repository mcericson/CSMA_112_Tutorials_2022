
def orientedText (annotation,x,y,Angle,font,fontsize,alignh,alignv,Color):
    #orients text off the base matrix, because of the 32 iteration limit of push matrix, this should be called only as a condition is met that closes the draw loop, allowing it to iterate once and only once. 
    #3.32.2018 Mark Ericson
    myFont =  createFont(font,12)
    noStroke()
    fill(Color)
    textFont(myFont)
    textSize(fontsize)
    pushMatrix()
    translate(x,y)
    rotate(radians(Angle))
    textAlign(alignh,alignv)
    text(annotation,0,0)
    popMatrix()
