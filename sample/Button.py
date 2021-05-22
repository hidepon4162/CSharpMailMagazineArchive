from machine import Pin
import utime

# led_external = Pin(15, Pin.OUT)

button = Pin(14, Pin.IN, Pin.PULL_DOWN)

# while True:
#     led_external.toggle()
#     utime.sleep(.5)
    
while True:
    if button.value() == 1:
        print("You pressed the button!")
        utime.sleep(2)