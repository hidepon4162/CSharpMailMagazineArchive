import math
from lcd.esp8266_i2c_lcd import I2cLcd, I2C

from lcd import *

from machine import Pin
from device.Input import Potentiometer

I2C_ADDR = 0x27
sda = Pin(0)
scl = Pin(1)

# I2C start
i2c = I2C(0, sda=sda, scl=scl, freq=400000)

lcdDisp = I2cLcd(i2c, I2C_ADDR, 2, 16)

potentiometer = Potentiometer(26)

while True:
    value = potentiometer.get_value()
    print(value)
    lcdDisp.move_to(0, 0)
    lcdDisp.putstr(str("{:03}".format(100 - math.floor(value))))
