from board import *
# GPIO
import digitalio
# Rotary Encoder
import rotaryio
# Keyboard
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

button = digitalio.DigitalInOut(D2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

encoder = rotaryio.IncrementalEncoder(D0,D1)
position = 0
last_position = 0
c = 97 # 'a'

keyboard_HID = Keyboard(usb_hid.devices)
keyboard_HID_layout = KeyboardLayoutUS(keyboard_HID)

while True:
     position = encoder.position
     if position != last_position:
         c = c + (position - last_position)
         if c > 127: # When over 'DEL'(127), change to 'SPC'(32).
            c = 32
         if c < 32: # When under 'SPC'(32), change to 'DEL'(127).
            c = 127
         print(chr(c))
     if not button.value:
         keyboard_HID_layout.write(chr(c))
         
     last_position = position
