import os
import sys
import RPi.GPIO as GPIO

togglePin = 15

GPIO.setwarnings (False)
GPIO.setmode (GPIO.BOARD)

GPIO.setup (togglePin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def call_pwr_toggle():
    os.system ('python control_pwr.py toggle')

def __main__():
    GPIO.add_event_detect (togglePin, GPIO.RISING, callback = call_pwr_toggle, bouncetime=200)
    while 1:
        time.sleep (1)

__main__()

#not clean up GPIO here since other scripts need to control GPIO
#GPIO.cleanup()

