from machine import Pin
import utime
import _thread

led_red = Pin(15, Pin.OUT)
led_amber = Pin(13, Pin.OUT)
led_green = Pin(12, Pin.OUT)

button = Pin(14, Pin.IN, Pin.PULL_DOWN)

global button_pressed
button_pressed = False

def button_reader_thread():
    global button_pressed
    while True:
        if button.value() == 1:
            button_pressed = True
        utime.sleep(0.01)
        
_thread.start_new_thread(button_reader_thread, ())
    
while True:
    if button_pressed == True:
        led_red.value(1)
        print("button")
        global button_pressed
        button_pressed = False

    led_red.value(1)
    utime.sleep(5)
    
    led_red.value(0)
    led_amber.value(0)
    led_green.value(1)
    
    utime.sleep(5)
    
    led_red.value(0)
    led_amber.value(1)
    led_green.value(0)
    
    utime.sleep(5)

    led_red.value(0)
    led_amber.value(0)
    led_green.value(0)
    

                