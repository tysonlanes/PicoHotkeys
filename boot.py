import storage, usb_cdc
import board, digitalio
import usb_midi

# Setup the button
button = digitalio.DigitalInOut(board.GP3)
button.pull = digitalio.Pull.UP

# Disable devices only if button is not pressed.
if button.value:
	storage.disable_usb_drive()
	usb_cdc.disable()
	usb_midi.disable()
