import os 

    
def save_pdf(make_pdf,file_name):
    #must call endrecord() at end of script
    #function must be called in setup

    if make_pdf == True:
        beginRecord( PDF ,"drawings/" + str(file_name) + str(hour()) + str(minute()) + 
                    str(month()) + str(day()) + str(year()) + ".pdf" )


def save_image(make_image,file_name):

    if make_image == True:
        save("drawings/" + str(file_name) + str(hour()) + str(minute()) + 
                    str(month()) + str(day()) + str(year()) + ".png" )
