from gpiozero import LED, Button
from time import sleep

count = 0

def incoming():
    global count
    count = count + 1
    print("Pressed", count)
    
key1 = Button(17)
pin = LED(16)

key1.when_pressed = incoming

while True:
    
    pin.on()
    sleep(1)
    pin.off()
    sleep(1)

