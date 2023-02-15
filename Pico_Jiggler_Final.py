import time
import board
import usb_hid
import random
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

# setup switch
sw1 = DigitalInOut(board.GP22)
sw1.direction = Direction.INPUT
sw1.pull = Pull.UP

# setup buttons
btn1 = DigitalInOut(board.GP28) # pin connected
btn1.direction = Direction.INPUT # no clue what this is for
btn1.pull = Pull.UP    # 4 pole clicky switches

btn2 = DigitalInOut(board.GP18) # pin connected
btn2.direction = Direction.INPUT # no clue what this is for
btn2.pull = Pull.UP    # 4 pole clicky switches

btn5 = DigitalInOut(board.GP1) # pin connected
btn5.direction = Direction.INPUT # no clue what this is for
btn5.pull = Pull.UP    # 4 pole clicky switches

# run the loop
while True:
    if sw1.value:
        led.value = True
        for x in range(random.randint(0, 3)):
            mse.move(50, 0, 0)
            time.sleep(random.uniform(0.2, 1.2))
            mse.move(0, 0, random.randint(-8, -3))
            time.sleep(random.uniform(0.8, 1.6))
            mse.move(0, -10, 0)
            mse.move(0, 0, random.randint(-18, -7))
            time.sleep(random.uniform(0.6, 3.8))
            mse.move(-50, 0, 0)
            time.sleep(random.uniform(2, 4.1))
            mse.move(0, 10, 0)
        mse.move(0, 0, random.randint(2, 7))
        time.sleep(random.uniform(0.2, 2.9))
        led.value = False
    if not btn1.value: # Button down status
        layout.write("Send this string of text\nin two lines!\n")
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
    else: # Button up status
        pass
    time.sleep(0.1)
