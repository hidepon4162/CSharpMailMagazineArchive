from machine import Pin
import utime

led_external = Pin(15, Pin.OUT)

while True:
    led_external.toggle()
    utime.sleep(.5)