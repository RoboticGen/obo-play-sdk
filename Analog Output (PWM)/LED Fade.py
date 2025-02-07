"""
Fade an LED using PWM on an ESP32 with MicroPython.
Connect an LED (with resistor) to GPIO15, for example.
"""

import machine
import time

# Configure PWM on GPIO15, 5000 Hz frequency
led_pin = machine.Pin(15)
pwm = machine.PWM(led_pin, freq=5000)

while True:
    # Fade up
    for duty_cycle in range(0, 1024, 8):  # from 0 to 1023 in steps
        pwm.duty(duty_cycle)
        time.sleep(0.01)
    # Fade down
    for duty_cycle in range(1023, -1, -8):
        pwm.duty(duty_cycle)
        time.sleep(0.01)
