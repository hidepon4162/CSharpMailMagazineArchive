from machine import Pin, ADC
import utime
import math

potentiometer = ADC(26)

conversion_factor = 3.3 / (65535)

while True:
    voltage = potentiometer.read_u16() * conversion_factor / 3.3 * 100
    ratio = math.floor(voltage)
    print(ratio)
    utime.sleep(.1)