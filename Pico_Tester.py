# Uses circuitpython 8.0.0

import time
import board
from digitalio import DigitalInOut, Direction, Pull

btn1 = DigitalInOut(board.GP3)
btn1.direction = Direction.INPUT
btn1.pull = Pull.UP

btn2 = DigitalInOut(board.GP7)
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP

sw1 = DigitalInOut(board.GP12)
sw1.direction = Direction.INPUT
sw1.pull = Pull.UP

while True:
    if not btn1.value:
        print("BTN1 is down")
    else:
        print("BTN1 is up")
    if not btn2.value:
        print("BTN2 is down")
    else:
        print("BTN2 is up")
    if not sw1.value:
        print("SW1 is off")
    else:
        print("SW1 is on")
    time.sleep(0.1)
