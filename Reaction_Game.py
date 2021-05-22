from machine import Pin
import utime
import urandom

pressed = False

led = Pin(15, Pin.OUT)

button = Pin(14, Pin.IN, Pin.PULL_DOWN)

def button_handler(pin):
    global pressed
    
    if not pressed:
        pressed = True
        print(pin)
   
button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)
   
led.value(1)

utime.sleep(urandom.uniform(5, 10))
led.value(0)


                
