# Uses MicroPython

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

with open("keylog.txt", "w") as logfile:
    while True:
        key_event = kbd.events.get()
        if key_event and key_event.keycode != Keycode.SPACEBAR:
            logfile.write(str(key_event.keycode) + "\n")
            logfile.flush()
