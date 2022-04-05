import m5stick as stick
import fusion
import time

def pitch_direction(pitch):
        if pitch > 80 and pitch < 90:
            return "right"
        if pitch > 0 and pitch < 5:
            return "up"
        if pitch > -90 and pitch < -80:
            return "left"
        if pitch > -10 and pitch < 0:
            return "down"

def roll_direction(roll):
        if roll < -80 and roll < - 90:
            return "front"
        if roll > 0 and roll < 5:
            return "up"
        if roll < 90 and roll > 80:
            return "back"
        if roll > 170 and roll < 180:
            return "down"

def stick_direction_distance():
    #create filter object
    filter = fusion.MahonyFilter()
    
    while True:
        #labels
        stick.print_to_screen("pitch", 0, 10)
        stick.print_to_screen("roll", 0, 140) 
        stick.print_to_screen("dist =" , 0, 105)
        
        #read imu and use fusion algo to obtain pitch and roll
        accel = stick.read_accelerometer()
        gyro  = stick.read_gyroscope()
        filter.update(accel,gyro)
        pitch = round(filter.pitch)
        roll  = round(filter.roll)
        
        #read information and print to screen
        stick.print_to_screen(pitch, 0, 40)
        stick.print_to_screen(roll, 0, 165)

        #if direction provided print to screen
        pitch_dir = pitch_direction(pitch)
        if pitch_dir:
            stick.print_to_screen(pitch_dir, 0, 70)
        roll_dir  = roll_direction(roll)
        if roll_dir:
            stick.print_to_screen(roll_dir, 0, 190)

        #read distance 
        distance = stick.read_sonar_distance()
        stick.print_to_screen(distance, 100, 105)
    
        lcd.clear()
   
stick_direction_distance()

