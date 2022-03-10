import m5stick as device
import tools
import time

# Constants for state
STATE_IDLE = 1
STATE_AWAKE = 2

state = STATE_IDLE


def update_display():
    if state == STATE_AWAKE:
        device.display_message("Hello.")
    elif state == STATE_IDLE:
        device.erase_screen()

    
while True:
    if device.button_pressed():
        if state == STATE_IDLE:
            state = STATE_AWAKE
        elif state == STATE_AWAKE:
            state = STATE_IDLE
    update_display() # This should be outside the if block so screen is refeshed each time
    time.sleep(0.5)
