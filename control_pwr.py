import sys
import RPi.GPIO as GPIO

#print "\n".join(sys.argv)

relayPin_0 = 11
relayPin_1 = 13

GPIO.setwarnings (False)
GPIO.setmode (GPIO.BOARD)

GPIO.setup (relayPin_0, GPIO.OUT)
GPIO.setup (relayPin_1, GPIO.OUT)

def power_on():
    GPIO.output (relayPin_0, GPIO.LOW)
    GPIO.output (relayPin_1, GPIO.LOW)

def power_off():
    GPIO.output (relayPin_0, GPIO.HIGH)
    GPIO.output (relayPin_1, GPIO.HIGH)

def power_toggle():
    if GPIO.input (relayPin_0):
        GPIO.output (relayPin_0, GPIO.LOW)
    else:
        GPIO.output (relayPin_0, GPIO.HIGH)
    if GPIO.input (relayPin_1):
        GPIO.output (relayPin_1, GPIO.LOW)
    else:
        GPIO.output (relayPin_1, GPIO.HIGH)

def __main__():
    if len(sys.argv) > 1:
        if sys.argv[1] == "on":
            power_on()
        elif sys.argv[1] == "off":
            power_off()
        elif sys.argv[1] == "toogle": 
            power_toggle()
    else:
        power_toggle() # default toggle


__main__()

#not clean up GPIO here since other scripts need to control GPIO
#GPIO.cleanup()

