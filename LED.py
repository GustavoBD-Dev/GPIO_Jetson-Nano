# import library
import RPi.GPIO as GPIO
import time

# Disable warnings
GPIO.setwarnings(False)

# Type of numeration (BOARD | BCM)
GPIO.setmode(GPIO.BOARD)

# Setting port 7 as output
GPIO.setup(7, GPIO.OUT)

while True:                 # infinite loop 
    GPIO.output(7, True)    # set out: 1.7V
    time.sleep(1)           # delay
    GPIO.output(7, False)   # set out: 0V
    time.sleep(1)           # delay