# Uses circuitpython
# add /adafruit_hid to root

import time
import board
import usb_hid
import random
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse

# setup a keyboard and mouse
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
mse = Mouse(usb_hid.devices)

btn1 = DigitalInOut(board.GP16) # pin connected
btn1.direction = Direction.INPUT # no clue what this is for
btn1.pull = Pull.UP    # 4 pole clicky switches

btn2 = DigitalInOut(board.GP18) # pin connected
btn2.direction = Direction.INPUT # no clue what this is for
btn2.pull = Pull.UP    # 4 pole clicky switches

btn3 = DigitalInOut(board.GP17) # pin connected
btn3.direction = Direction.INPUT # no clue what this is for
btn3.pull = Pull.UP    # 4 pole clicky switches

btn4 = DigitalInOut(board.GP20) # pin connected
btn4.direction = Direction.INPUT # no clue what this is for
btn4.pull = Pull.UP    # 4 pole clicky switches

btn5 = DigitalInOut(board.GP19) # pin connected
btn5.direction = Direction.INPUT # no clue what this is for
btn5.pull = Pull.UP    # 4 pole clicky switches

btn6 = DigitalInOut(board.GP21) # pin connected
btn6.direction = Direction.INPUT # no clue what this is for
btn6.pull = Pull.UP    # 4 pole clicky switches

while True:
    if not btn1.value: # Button down status
        kbd.press(Keycode.SHIFT)
        time.sleep(0.05)
        kbd.press(Keycode.ALT)
        time.sleep(0.05)
        kbd.send(Keycode.P)
        time.sleep(0.05)
        kbd.release(Keycode.SHIFT, Keycode.ALT)
        time.sleep(0.02)
    if not btn2.value:
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
    if not btn3.value:
        layout.write("This is a test string!\nYou can put anything you want here.\n")
    if not btn4.value:
        kbd.send(Keycode.FOUR)
    if not btn5.value:
        while True:
            if btn6.value:
                for x in range(random.randint(0, 3)):
                    if not btn6.value:
                        break
                    mse.move(50, 20, 0)
                    if not btn6.value:
                        break
                    time.sleep(random.uniform(0.2, 1.2))
                    if not btn6.value:
                        break
                    mse.move(0, 0, random.randint(-8, -3))
                    if not btn6.value:
                        break
                    time.sleep(random.uniform(0.8, 1.6))
                    if not btn6.value:
                        break
                    mse.move(-40, -10, 0)
                    if not btn6.value:
                        break
                    mse.move(0, 0, random.randint(-18, -7))
                    if not btn6.value:
                        break
                    time.sleep(random.uniform(0.6, 3.8))
                    if not btn6.value:
                        break
                    mse.move(-10, -10, 0)
                    if not btn6.value:
                        break
                    time.sleep(random.uniform(2, 4.1))
                    if not btn6.value:
                        break
                mse.move(0, 0, random.randint(2, 7))
                if not btn6.value:
                        break
                time.sleep(random.uniform(0.2, 2.9))
            if not btn6.value:
                break
    else: # Button up status
        pass
    time.sleep(0.1)
    
