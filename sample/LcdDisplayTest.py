import time
import machine
from esp8266_i2c_lcd import I2cLcd

I2C_ADDR = 0x27
sda = machine.Pin(0)
scl = machine.Pin(1)

#I2C start
i2c = machine.I2C(0, sda = sda, scl = scl, freq = 400000)
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
lcd.putstr("It Works!\nSecond Line")
time.sleep(3)
lcd.clear()
time.sleep(3)
lcd.putstr("Hello\nI'm METAELE")