import sys
import RPi.GPIO as GPIO

print "\n".join(sys.argv)

relayPin_0 = 11
relayPin_1 = 13

GPIO.setwarnings (False)
GPIO.setmode (GPIO.BOARD)

GPIO.setup (relayPin_0, GPIO.OUT)
GPIO.setup (relayPin_1, GPIO.OUT)

if sys.argv[1] == "on":
    GPIO.output (relayPin_0, GPIO.LOW)
    GPIO.output (relayPin_1, GPIO.LOW)
elif sys.argv[1] == "off":
    GPIO.output (relayPin_0, GPIO.HIGH)
    GPIO.output (relayPin_1, GPIO.HIGH)

#GPIO.cleanup()

