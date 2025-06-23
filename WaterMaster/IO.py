import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.cleanup()
pin = 16

gpio.setup(pin, gpio.OUT, initial=gpio.LOW)

time.sleep(10)
gpio.output(pin, gpio.HIGH)

print("finished")
