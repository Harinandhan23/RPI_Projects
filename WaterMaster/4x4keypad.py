from gpiozero import LED, Button

#import RPi.GPIO as GPIO
import time

# Set the Row Pins
ROW_1 = 6
ROW_2 = 13
ROW_3 = 19
ROW_4 = 26

# Set the Column Pins
COL_1 = 12
COL_2 = 16
COL_3 = 20
COL_4 = 21


# Set Row pins as output
row1 = LED(ROW_1)
row2 = LED(ROW_2)
row3 = LED(ROW_3)
row4 = LED(ROW_4)

# Set column pins as input and Pulled up high by default
col1 = Button(COL_1)
col2 = Button(COL_2)
col3 = Button(COL_3)
col4 = Button(COL_4)

# function to read each row and each column
def readRow(line, characters):
    line.off()
    if col1.is_pressed:
        print(characters[0])
    if col2.is_pressed:
        print(characters[1])
    if col3.is_pressed:
        print(characters[2])
    if col4.is_pressed:
        print(characters[3])
    line.on()

# Endless loop by checking each row 
try:
    while True:
        readRow(row1, ["1","2","3","A"])
        readRow(row2, ["4","5","6","B"])
        readRow(row3, ["7","8","9","C"])
        readRow(row4, ["*","0","#","D"])
        time.sleep(0.2) # adjust this per your own setup
except KeyboardInterrupt:
    print("\nKeypad Application Interrupted!")
    GPIO.cleanup()
