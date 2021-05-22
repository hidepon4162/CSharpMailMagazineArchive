import machine
import utime
from esp8266_i2c_lcd import I2cLcd

print("A")
I2C_ADDR = 0x27
sda = machine.Pin(0)
scl = machine.Pin(1)

#I2C start
i2c = machine.I2C(0, sda = sda, scl = scl, freq = 400000)
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temprature = 27 - (reading - 0.706) / 0.001721
    lcd.putstr("Class Room\nTemp. " + str("{:.1f}".format(temprature)) + "C")
    utime.sleep(10)
    lcd.clear()
    print (temprature)