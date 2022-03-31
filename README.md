# M5Stick C Plus Guide

This guide will help you to get started using your m5stick c plus.

## Class Links

- **Moodle:** https://moodle.woodbury.edu/course/view.php?id=14537

- **Lecture 1:**  https://docs.google.com/presentation/d/1i-4nHaGF4E_G2huGPWdVJgdik4sVa5KhXWHyBsRo1dE/edit?usp=sharing

- **Lecture 2:**  https://docs.google.com/presentation/d/138RcZcWDxsSt7d3pblK6qECbQne3d8ST8vznfT1NVb0/edit?usp=sharing

## External Links

- **Quick Start Guide for M5stick** This provides information on burning, and using the buttons on the stick. https://docs.m5stack.com/en/quick_start/m5stickc/uiflow

- **Micropython for the M5Stick:**  https://github.com/m5stack/M5Stack_MicroPython

- **Micropython Documentation:**  https://docs.micropython.org/en/latest/esp32/quickref.html#

- **M5Flow On-line Editor:** The default mode for the m5flow editor is blocky.  However if open a demo file from the pull-down menu, you can switch to python mode and see the python implementation of the module. https://flow.m5stack.com/

- **UIflow Documentation:** This is the documentation for the UIflow code editor.  Fork this repository and save it to your Github desktop.  Open the M5Flow online editor.  Select the open file icon in the upper right hand corner of the editor and and navigate to the example that you would like to open.  The sonic sensor and all other external sensors can be found in the "Unit" folder. The editor will open the file as blocky example.  Toggle to python mode and you will see the example written in python. https://github.com/m5stack/M5-ProductExampleCodes

- **Quick Start:** https://m5guide.readthedocs.io/da/latest/.

- **Accessing Built-in Modules with REPL:**  Read Evaluate Print Loop or REPL offers a way of interfacing with the stick via a terminal. It also allows you to access and see all of the modules and libraries that are on the stick.  This video explains the process:  https://www.youtube.com/watch?v=V67MY-1ccqM

-**Alternate IDE // Thonny:** Another IDE that works well with m5Stack is Thonny.  You can download it here: https://thonny.org/ You can also watch this video on how to connect and run programs on the stick: https://www.youtube.com/watch?v=YEQPAK609Uo


## Terminology
- **Non-volatile memory**: Information that is written into memory such as a solid state drive that will persist after the power is switched off (ROM).

- **Volatile memory**: Information that is created by a program and will disappear once the power is switched off (RAM).

- **Flash Memory**: This is a form of non-volatile memory that can be electrically erased and reprogrammed.

- **Hardware**: The physical construction of the computer including its motherboard, CPU, RAM, power supply, GPU, and sound card.

- **Software**: A program that provides the computer instructions to complete a specific task.

- **Embedded Software**: This a type of program that performs a simple task on specific device that we don't normally think of as a computer.

- **Application Software**:  Is a piece of software that provides functionality on top of the operating system.

- **Firmware**: A type of software that is closely tied to the hardware of a specific device. It is typically stored in ROM or Read Only Memory, meaning that it remains loaded when a device is powered off. As a result, it appears to be etched directly into hardware.

- **microcontroller**: This is a small computer that is typically programmed to perform a simple task.

- **Flashing**: This is process of writing a program to the flash memory of a microcontroller. 

## M5 Stick C Plus

- **Hardware**: ESP32 Pico with 4mb of Flash memory and 512 kb of RAM. Microphone, speaker, LCD, LED and accelerometer are all part of the hardware.

- **Firmware**: M5stick library "burned" to device with M5 burner

- **Embedded Software**: Flashed to the device by saving with the IDE.

## Getting Started

- Download and install M5burner:  https://shop.m5stack.com/pages/download

- Download and install VSCode: https://code.visualstudio.com/

- Follow the class example to use the  M5 burner to burn the firmware to the m5stick. You will need your network id and password  Here is a guide: https://docs.m5stack.com/en/quick_start/m5stickc_plus/mpy

- **VSCODE** Open up VScode and navigate the "extensions" palette on the left hand side of the window and search for m5stack.  Install the extension: curdeveryday.vscode-m5stack-mpy

- **Quick Start Guide for M5stick** This provides information on burning, and using the buttons on the stick. https://docs.m5stack.com/en/quick_start/m5stickc/uiflow

- **M5Stick** Set the m5stick to USB mode.  To do this, turn the power on by holding the lower left button, and then quickly press the upper right button. The setting window should open. Use the right button to scroll through options and the left button to select.  Select "switch mode" and then navigate to "USB" and select. Return to the main menu and and select "Reboot"

- **VSCODE** Plug-in your m5stick to the usb-c cable. Connect it by clicking on the "Add M5stack" at the lower left hand corner of your screen. Once you select this a window should pop-up asking you to select the comm port. Simply check the box a click "ok".

- **VSCODE** On the left hand side navigate of the VSCODE window and select M5Stick. 

- **VSCODE** Navigate to the "File Explorer" tab on the left hand side tool bar and click on it. 

- **VSCODE** Scroll Down to the "M5STACK DEVICE" and expand it.  It should reveal the file structure that currently exists on the device. 


## File Structure

- **main.py** There several folders and files within the existing structure.  You can save files of any name to the folder and run them with **VSCODE**, but to flash a file to the stick and have it run when the stick boots up it needs to be saved as main.py in outermost directory (not in a folder).

- **Create a File** To create file hit the **+** sign at next to any of the folders. Name the file "name.py".  Open the file.

- **Save a File** Alternatively you can create file on your computer and save it to he M5Stick.  To do this select the icon with file drawer and up arrow "upload". Select a file from your computer and it should appear in the device.


## First Program

- **Documentation** The best documentation can be found at this the link below. Importantly, you need to have google translate it to English from the original Danish:  “M5 MicroPython Guide - M5 Guide Documentation.” n.d. Accessed January 10, 2022. https://m5guide.readthedocs.io/da/latest/.

- **VSCODE** Create a folder on your computer.  In VSCODE, from the file pulldown menu, open the folder.  Next to the folder name select the **+** sign and add file to the folder. Name the file by right clicking on the file and selecting rename.  Add the name and the file extension ".py".

- **VSCODE** Add the following lines to your python file.
```python

from m5stack import *
from m5ui import *
from uiflow import *


setScreenColor(0xff0000)

```

- **VSCODE** Import this file onto your M5Stick by uploading to the folder "apps".

- **VSCODE** Once the file appears in the folder "apps" open the file and select the solid play arrow in the upper right hand corner of your window.  If it is working, the screen on your M5stick should turn red. 

## Second Program

 - **Hexadecimal Color** In the previous example we used the RGB color model with hexadecimal color notation.  In another class we will go over the way the notation system works, but for today is sufficient to note that hexadecimal notation stores the values of RGB (0-255) in hexadecimal pairs ranging from 00 - ff. The M5stick requires the addition of "0x" + the hexadecimal notation to specify a color For example:

 ```python

 red   =    0xff0000
 green =    0x00ff00
 blue  =    0x0000ff

 ```

- **VSCODE** The next program that we will create will make the stick flash from red to green to blue and then repeat a set number of times. To this we will need to use the time library. Importantly, we are no longer working in Processing so the "pulse" of the draw loop is something that we have to create ourselves. 

- **VSCODE** In the outermost directory of the M5 stick make a new file called set_color.py. Open the file. Add the following imports to the head of document:

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time

```

- **VSCODE** Now we need to write a program that creates a color and then pauses. To do that we will use the m5stick function setScreenColor() and the time function time.sleep_ms():

```python

def color_pause(color,duration):
    
    setScreenColor(color)
    time.sleep_ms(duration)
    
```

- **VSCODE** If we were working in Processing we could just use the draw() loop to execute this code.  Since we are not, we will need to make our own loop.  To do this we will use  a "while" loop.  This loop will run until a condition is met and we can create a stopping point by adding a counter:

```python
def flash_rgb(duration, stop):
    count = 0
    while count < stop:
        
        count += 1
        color_pause(0xff0000, duration)
        color_pause(0x00ff00, duration)
        color_pause(0x0000ff, duration)
```

- **VSCODE** Next we will open the main.py program and replace the existing code with:

```python
import set_color 

set_color.flash_rgb(500,10)
```

This will import our set_color module and call the flash_rgb() function.  Asking the computer to render the screen in a red and pause 500 ms, Green and pause 500 ms, and Blue and pause 500 ms.  The code will run a total of 10 times. 

 # m5Stick Builtin Modules
 

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

```
## ESP32 

The board of the m5Stick is the ESP32. Full documentation of the micropython libraries associated with the board can be found here: https://docs.micropython.org/en/latest/esp32/quickref.html#

```python

#example of accessing the boards internal temperature:

import esp32

data = esp32.raw_temperature()

lcd.clear()
lcd.text(5,5, str(data))

```
# External Sensors

## Ultrasonic Sensor

- **link to documentation:** https://docs.m5stack.com/en/unit/sonic

```python

from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit


sonar = unit.get(unit.ULTRASONIC, unit.PORTA)

while True:

    lcd.clear(0x000000)
    dist = str(sonar.distance)
    lcd.print(dist,10,20)
    time.sleep(1)

```



 


