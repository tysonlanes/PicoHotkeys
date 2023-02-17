# Uses circuitpython 8.0.0

import time
import board
import usb_hid
import random
import EDIT_ME
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse

# setup onboard LED
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = False

# setup a keyboard and mouse
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
mse = Mouse(usb_hid.devices)

# setup the buttons
btn1 = DigitalInOut(board.GP3)
btn1.direction = Direction.INPUT
btn1.pull = Pull.UP

btn2 = DigitalInOut(board.GP7)
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP

# setup teh switch - 3 pin with logic in middle and ground on either side.
# switch toward ground is off position, toward logic is on.
sw1 = DigitalInOut(board.GP12)
sw1.direction = Direction.INPUT
sw1.pull = Pull.UP

# run the loop
while True:
    if sw1.value: # Switch in on position - This is the mouse jiggler
        led.value = True # turn on the onboard LED
        for x in range(random.randint(0, 3)): # Introduce ramdomness for AI watching for jigglers
            mse.move(50, 0, 0) # move mouse down 50 units
            if not sw1.value: # Check to see if switch in off position
                led.value = False # turn LED off
                break # escape the for loop and return to main while true loop
            time.sleep(random.uniform(0.2, 1.2)) # wait random time
            mse.move(0, 0, random.randint(-8, -3)) # scroll mouse wheel random amount of units down
            if not sw1.value:
                led.value = False
                break
            time.sleep(random.uniform(0.8, 1.6))
            mse.move(0, -10, 0) # move mouse 10 units to the left
            mse.move(0, 0, random.randint(-18, -7))
            if not sw1.value:
                led.value = False
                break
            time.sleep(random.uniform(0.6, 3.8))
            mse.move(-50, 0, 0)
            if not sw1.value:
                led.value = False
                break
            time.sleep(random.uniform(2, 4.1))
            mse.move(0, 10, 0)
        mse.move(0, 0, random.randint(2, 7))
        time.sleep(random.uniform(0.2, 2.9))
        led.value = False
    if not btn1.value: # Button down status - This sends the string found in /sender.py
        layout.write(EDIT_ME.CHANGE_ME)
    if not btn2.value: # Button down status - This sends the hotkey to the grabbing tool grab selection
        kbd.press(Keycode.SHIFT)
        time.sleep(0.05)
        kbd.press(Keycode.WINDOWS)
        time.sleep(0.05)
        kbd.send(Keycode.S)
        time.sleep(0.05)
        kbd.release(Keycode.SHIFT)
        time.sleep(0.02)
        kbd.release(Keycode.WINDOWS)
        time.sleep(0.02)
    else: # Switch off and buttons not pressed
        pass
    time.sleep(0.1)
