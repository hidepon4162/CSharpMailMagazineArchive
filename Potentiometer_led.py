from machine import Pin, ADC, PWM
import utime
import math

potentiometer = ADC(26)

led = PWM(Pin(15))

led.freq(1000)

conversion_factor = 3.3 / (65535)

while True:
    voltage = potentiometer.read_u16() * conversion_factor / 3.3 * 100
    ratio = math.floor(voltage)
    print(ratio)
    led.duty_u16(potentiometer.read_u16())
    utime.sleep(.1)
