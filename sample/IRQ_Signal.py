from machine import Pin
import utime
import urandom

pressed = False

led_red = Pin(15, Pin.OUT)
led_amber = Pin(13, Pin.OUT)
led_green = Pin(12, Pin.OUT)


button = Pin(14, Pin.IN, Pin.PULL_DOWN)

def button_handler(pin):
    global pressed
    
    pressed = not pressed
    
    if pressed == True:
        led_red.low()
        led_amber.low()
        led_green.low()
        utime.sleep(0.01)
#         pressed = True
    
    print(pressed)
   
button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)

def led_loop():

    while True:
        if pressed:
            return
        
        if not pressed:
            led_red.high()
            led_amber.low()
            led_green.low()
            
            utime.sleep(1)
            
        if not pressed:
            led_red.low()
            led_amber.high()
            led_green.low()
            
            utime.sleep(1)
            
        if not pressed:
            led_red.low()
            led_amber.low()
            led_green.high()
            
            utime.sleep(1)
#         led_red.toggle()
#         led_amber.toggle()
#         led_green.toggle()

while True:
    led_loop()

# utime.sleep(urandom.uniform(5, 10))


                

