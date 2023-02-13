# Uses circuitpython 8.0.0

import time
import board
from digitalio import DigitalInOut, Direction, Pull

btn = DigitalInOut(board.GP16)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

while True:
    if not btn.value:
        print("BTN is down")
    else:
        print("BTN is up")
    time.sleep(0.1)
