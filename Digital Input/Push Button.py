"""
Read a push button on an ESP32 using MicroPython.
Connect a button between GPIO4 and GND, and use an internal pull-up resistor.
"""

import machine
import time

# Configure GPIO4 as input with an internal pull-up
button_pin = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    button_state = button_pin.value()
    if button_state == 0:
        print("Button Pressed!")
    else:
        print("Button Released!")
    time.sleep(0.2)  # check 5 times per second
