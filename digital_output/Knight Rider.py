"""
Knight Rider / LED chase effect on an ESP32 using multiple GPIO pins.
Connect a series of LEDs (with resistors) to consecutive GPIOs.
"""

import machine
import time

# Choose a set of GPIO pins for the LEDs
led_pins = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in (12, 13, 14, 15)]

delay = 0.5  # seconds between steps

while True:
    # Move "forward" across the LED array
    for i in range(len(led_pins)):
        # Turn on current LED
        led_pins[i].value(1)
        time.sleep(delay)
        # Turn off current LED
        led_pins[i].value(0)

    # Move "backward" across the LED array
    for i in reversed(range(len(led_pins))):
        led_pins[i].value(1)
        time.sleep(delay)
        led_pins[i].value(0)
