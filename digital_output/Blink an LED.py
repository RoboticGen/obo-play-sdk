"""
Blink an LED on an ESP32 using MicroPython.
Connect an LED (with resistor) to GPIO2 or use the built-in LED on some boards.
"""

import machine
import time

# Configure GPIO2 as an output
led_pin = machine.Pin(2, machine.Pin.OUT)

while True:
    led_pin.value(1)  # LED ON
    time.sleep(1)
    led_pin.value(0)  # LED OFF
    time.sleep(1)
