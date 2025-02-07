"""
Read a potentiometer on an ESP32 using MicroPython.
Connect the pot's wiper to GPIO34 (an ADC-capable pin), 
and the other terminals to 3.3V and GND.
"""

import machine
import time

# Configure GPIO34 as an ADC input
pot_pin = machine.ADC(machine.Pin(34))
pot_pin.atten(machine.ADC.ATTN_11DB)  # allows reading up to ~3.3V

while True:
    pot_value = pot_pin.read()  # read 0-4095
    voltage = (pot_value / 4095) * 3.3
    print("Pot Value:", pot_value, "Approx Voltage:", voltage)
    time.sleep(0.5)
