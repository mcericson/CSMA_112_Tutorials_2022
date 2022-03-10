import m5stick as device
import tools
import time


awake = False # State


def update_display():
    if awake:
        device.display_message("Hello.")
    else:
        device.erase_screen()

    
while True:
    if device.button_pressed():
        awake = not awake # Toggle to new state
    update_display() # This should be outside the if block so screen is refeshed each time
    time.sleep(0.5)
