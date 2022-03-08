 # 220308 m5Stick Builtin Modules

 ## Screen

- **lcd:** lcd is the class from which all function related to the screen can be called. 

- **screen size:**  80 x 160 pixels. To get the current screen size:

```python

width, height = lcd.screensize()

```

- **origin:** (0,0) is always located in the upper left of the screen depending on orientation.
 - **orientation:** The screen can be oriented based on the following commands.

 ```python

 lcd.orient(lcd.PORTRAIT)
 lcd.orient(lcd.PORTRAIT_FLIP)

 lcd.orient(lcd.LANDSCAPE)
 lcd.orient(lcd.LANDSCAPE_FLIP)

 ```

 - **drawing:** 

 ```python

lcd.rect(x, y, height, width, color, fillcolor) #rectangle 

#example 

lcd.rect(0,0, 10, 20, color=0xFF0000, fillcolor=0x00FF00) #Draws a 10 x 20 pixel rectangle withe the first corner at (0,0) a red stroke and a green fill.

lcd.roundrect(x, y, height, width, r, color, fillcolor) #rectangle with round corners

lcd.line (x1, y1, x2, y2, color) #line

lcd.triangle(x1, y1, x2, y2, x3, y3, color, fillcolor) #triangle

lcd.ellipse(x, y, width, height, opt, color, fillcolor ) #ellipse the opt call declares how much of the ellipse to be drawn. 15 is equal to a full ellipse

lcd.circle(x, y, radius, color, fillcolor) #circle 

lcd.arc(x, y, radius, thickness, start, end, color) #arc cannot be filled. Thickness is equivalent to stroke weight.

lcd.polygon(x, y, radius, sides, thickness, color, fill color, rotate) #regular polygon

lcd.pixel(x, y, color) #turns a single pixel on. White is the default value. 

lcd.image(x, y, filename)# loads an image that is stored on the m5Stick. .bmp and .jpg formats only.

lcd.text(x, y, msg, color, transparent=True)#displays text to the screen at a specified location.

#example:
lcd.text(0,0, "Don't print hello!", color=0x0000FF) 

lcd.font(lcd.FONT_fontname):

#example:

lcd.font(lcd.FONT_Ubuntu)

#default fonts:

lcd.font(lcd.FONT_Default)

lcd.font(lcd.FONT_DefaultSmall)

lcd.font(lcd.FONT_DejaVu18)

lcd.font(lcd.FONT_DejaVu24)

lcd.font(lcd.FONT_DejaVu40)

lcd.font(lcd.FONT_DejaVu56)

lcd.font(lcd.FONT_DejaVu72)

lcd.font(lcd.FONT_Ubuntu)

lcd.font(lcd.FONT_Comic)

```

## LED
The m5Stick has a built in LED light in the upper left hand corner

```python

from m5stack import M5led

#turn on light
M5Led.on()

#turn off light
M5Led.off()
```
## Buttons
 There are two programmable buttons on the m5Stick. Button A is the button with the M5 logo on it. Button B is th upper right hand corner of the m5Stick.  The on/off button (lower left) cannot be be programmed.

```python

from m5Stack import btnA

btnA.wasPressed() #returns a boolean. Pressed is True.
```
## Buzzer
The m5Stick includes a buzzer.  This device is capable of producing a tone at frequency with a set volume.

```python
from m5stack import speaker

speaker.setVolume(1)
speaker.sing(220,  1)

```


## Accelerometer and Gyroscope
The m5Stick includes an inertial measurement unit called an IMU.  The IMU can detect:

- rotation speed
- rate of acceleration or deceleration 
- direction of gravity 

- The orientation of the screen can be found with the following accelerometer values:

- flat on back = (0.0, 0.0, 1.0)
- on left side = (1.0, 0.0, 0.0)
- vertical  = (0.0, 1.0, 0.0)

- **accelerometer**
```python

import imu

stick_IMU = imu.IMU()

#get the x, y, and z values of acceleration
ax, ay, az = stick_IMU.acceleration

```
- **gyroscope**

```python

import IMU

stick_IMU = imu.IMU()

#get the x, y, and z values of rotation
gx, gy, gz = stick_IMU.gyro

## ESP32 

The board of the m5Stick is the ESP32. Full documentation of the micropython libraries associated with the board can be found here: https://docs.micropython.org/en/latest/esp32/quickref.html#

```python

#example of accessing the boards internal temperature:

import esp32

data = esp32.raw_temperature()

lcd.clear()
lcd.text(5,5, str(data))

```




 


