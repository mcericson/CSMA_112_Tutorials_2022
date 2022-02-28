# 220301 Class Notes

This guide will help you to get started using your m5stick c plus.

## Terminology
- **Nonvolatile memory**: Information that is etched into the board and will remain after the power is switched off(ROM)

- **Volatile memory**: Information that is created by a program and will disappear once the power is switched off(RAM).

- **Flash Memory**: This is a form of non-volatile memory that can be electrically erased and reprogrammed.

- **Hardware**: The physical construction of the computer including its motherboard, CPU, RAM, power supply, GPU, and sound card.

- **Software**: A program that provides the computer instructions to complete a specific task.

- **Embedded Software**: This a type of program that performs a simple task on specific device, performing as the operating system itself.

- **Application Software**:  Is a piece of software that provide functionality on top of the operating system.

- **Firmware**: A type of software that is etched directly into the hardware. It is typically stored in ROM or Read Only Memory.

- **microcontroller**: This is a small computer that is typically programmed to perform a simple task.

- **Flashing**: This is process of writing a program to the flash memory of a microcontroller. 

## M5 Stick C Plus

**Hardware**: ESP32 Pico with 4mb of Flash memory and 512 kb of RAM. Microphone, speaker, LCD, LED and accellerometer are all part of the hardware.

**Firmware**: M5stick library "burned" to device with M5 burner

**Embedded Software**: Flashed to the device by saving with the IDE.

## Getting Started

- Download and install M5burner:  https://shop.m5stack.com/pages/download

- Download and install VSCode: https://code.visualstudio.com/

- Follow the class example to use the  M5 burner to burn the firmware to the m5stick. You will need your network id and password  Here is a guide: https://docs.m5stack.com/en/quick_start/m5stickc_plus/mpy

- **VSCODE** Open up VScode and navigate the "extensions" palette on the left hand side of the window and search for m5stack.  Install the extension: curdeveryday.vscode-m5stack-mpy

- **M5Stick** Set the m5stick to USB mode.  To do this, turn the power on by holding the lower left button, and then quickly press the upper right button. The setting window should open. Use the right button to scroll through options and the left button to select.  Select "switch mode" and then navigate to "USB" and select. Return to the main menu and and select "Reboot"

- **VSCODE** Plug-in your m5stick to the usb-c cable. Connect it by clicking on the "Add M5stack" at the lower left hand corner of your screen. Once you select this a window should pop-up asking you to select the comm port. Simply check the box a click "ok".

- **VSCODE**On the left hand side navigate of the VSCODE window and select M5Stick




