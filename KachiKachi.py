from board import *
import busio
import time
# GPIO
import digitalio
# Rotary Encoder
import rotaryio
# Keyboard
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
# SSD1306
import adafruit_ssd1306

button = digitalio.DigitalInOut(D2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

encoder = rotaryio.IncrementalEncoder(D0,D1)
position = 0
last_position = 0
c = 97 # 'a'

keyboard_HID = Keyboard(usb_hid.devices)
keyboard_HID_layout = KeyboardLayoutUS(keyboard_HID)

i2c = busio.I2C(D5, D4)  # (SCL, SDA)5,4
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)


while True:
     display.fill(0)
     display.text(chr(c), 3, 0, True, font_name="font5x8.bin", size=8)
     display.show()
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
         time.sleep(0.4) # Avoid deboucing
         
     last_position = position
