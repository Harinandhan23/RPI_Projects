from pcf8575 import PCF8575
from gpiozero import Button
import time

def SwitchLed(portNo, value):
    global pcf
    pcf.port[portNo] = value

def TroubleShootLed(portList):  
    for i in portList:
        SwitchLed(portList.index(i), True)
        time.sleep(1)
        SwitchLed(portList.index(i), False)

def button_irq_handler():
    global pcf
    print(pcf.port)

def init_pcf(values):
    global pcf
    for i in range(16):
        #pcf.port[i] = False # for led
        pcf.port[i] = True # for button
        #print(values[i])
        
def initialisePCF_ports(pcfObject, portIndex, value):
    for portCount in range(8):
        pcfObject.port[portIndex] = value
        portIndex += 1
    print(pcfObject.port)

i2c_port = 1
address = 0x21

button_irq = Button(21)

pcf_port = ["p17", "p16", "p15", "p14", "p13", "p12", "p11", "p10", \
            "p07", "p06", "p05", "p04", "p03", "p02", "p01", "p00"]

pcf = PCF8575(i2c_port, address)

button_irq.when_released = button_irq_handler

#init_pcf(pcf_port)

initialisePCF_ports(pcf, pcf_port.index("p07"), True)

#TroubleShootLed(pcf_port)

print("init complete")
while True:
    pass
