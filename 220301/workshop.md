# 220301 Class Notes

This guide will help you to get started using your m5stick c plus.

## Terminology
- **Non-volatile memory**: Information that is written into memory such as a solid state drive that will persist after the power is switched off (ROM).

- **Volatile memory**: Information that is created by a program and will disappear once the power is switched off (RAM).

- **Flash Memory**: This is a form of non-volatile memory that can be electrically erased and reprogrammed.

- **Hardware**: The physical construction of the computer including its motherboard, CPU, RAM, power supply, GPU, and sound card.

- **Software**: A program that provides the computer instructions to complete a specific task.

- **Embedded Software**: This a type of program that performs a simple task on specific device that we don't normally think of as a computer.

- **Application Software**:  Is a piece of software that provide functionality on top of the operating system.

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