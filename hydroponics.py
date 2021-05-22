from machine import Pin
from lcd.esp8266_i2c_lcd import I2cLcd, I2C
from lcd import *
from device.Input import Potentiometer, Soilsensor

import utime

# I2C
I2C_ADDR = 0x27
sda = Pin(0)
scl = Pin(1)

# I2C start
i2c = I2C(0, sda=sda, scl=scl, freq=400000)

lcdDisp = I2cLcd(i2c, I2C_ADDR, 2, 16)

# Motor
relay = Pin(2, Pin.OUT, Pin.PULL_DOWN)
motorOn = 0
motorOff = 1

# 土壌湿度センサー
senser = Soilsensor(2, 0.9, 1.0)

# センサー情報取得間隔
fillWaterTimeSpan = 0.1
enoughWaterTimeSpan = 0.2


def check_watersSurface():
    if reading == True:
        warningDisp = "Empty "
        timeSpan = fillWaterTimeSpan
        relay.value(motorOn)
    else:
        warningDisp = "Enough"
        timeSpan = enoughWaterTimeSpan
        relay.value(motorOff)
    return warningDisp, timeSpan


while True:
    reading = senser.get_needWater()

    print(reading)

    warningDisp, timeSpan = check_watersSurface()

    utime.sleep(timeSpan)

    lcdDisp.move_to(0, 0)
    lcdDisp.putstr(warningDisp)
