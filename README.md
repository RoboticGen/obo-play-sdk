# OBO-Play SDK Documentation
<p align="center">

<img width="100%" src="https://github.com/RoboticGen/obo-play-sdk/blob/main/IMG/OBO%20Play%20PitchDeck.png" text="OBO PLAY">
  <p align="center">
    </p> 


---
This repository provides sample code and documentation for the **Obo-Play Kit**.


## Features

- **OLED Display Control:** Initialize the SSD1306 display over I2C, clear the screen, display text, and even draw images.
- **Easy Setup:** Step‑by‑step instructions to flash MicroPython and upload the files via Thonny IDE.

---

## Prerequisites

1. **Install Thonny IDE**:

   - Download and install Thonny IDE from [Thonny.org](https://thonny.org/).

2. **Install MicroPython on ESP32**:

   - Open Thonny IDE.
   - Go to `Run -> Configure Interpreter`.
   - In the "Interpreter" section, select:
     - **MicroPython (ESP32)** under "MicroPython family."
     - For the "Port," choose **< Try to detect port Automatically >**
   - Click **Install or update MicroPython (esptool)**.
   - Choose:
     - For the "Target Port," choose the correct **Target Port** for your ESP32 (e.g., `COM3`, `COM4`, `/dev/ttyUSB0`).
     - **MicroPython family**: ESP32.
     - **Variant**: Espressif ESP32 / WROOM.
   - Click **Install** to flash MicroPython onto your ESP32.


3. **Upload the Test Code**:
   - Create a new file in Thonny.
   - Copy the contents of `main.py` into the file.
   - Click Save
   - Select 'Micropython device'
   - Rename as `main.py`
   - Select OK
   - Extra : If a dialogue box appeared asking overwriting click OK


Once MicroPython is installed, you can connect to the ESP32 via Thonny and start using the SDK. Continue with the usage examples and SDK features listed above!

---

## Troubleshooting MicroPython on ESP32

If you encounter issues such as a **"Backend not ready"** warning or the program seems stuck, follow these steps to reset your ESP32:

1. **Press the Stop Button**:

   - In Thonny, click the red **Stop** button located at the top to interrupt any running code.

2. **Reset via Shell**:

   - If pressing the stop button doesn’t resolve the issue:
     - Make sure you do not click or interact with the shell section in Thonny.
     - Instead, press **Ctrl + C** twice in quick succession to force a reset of the ESP32.

3. **Reconnect the Device**:

   - If the device still doesn't respond, unplug and replug your ESP32.
   - Go to `Run -> Configure Interpreter` and verify the **Target Port** is still correctly set.

4. **Reinstall MicroPython** (Optional):
   - If the problem persists, you may need to reinstall MicroPython using the instructions provided above.

With these steps, you should be able to regain control of your ESP32 and continue using the OBOPlay SDK.

---

## Examples Overview

### [1. Blink an LED](https://github.com/RoboticGen/obo-play-sdk/blob/main/digital_output/Blink%20an%20LED.py)

Toggles an LED on and off at 1-second intervals, demonstrating a simple digital output.
![3](https://github.com/RoboticGen/obo-play-sdk/blob/main/IMG/415965245-3081c151-39a7-4ece-959b-c5b6539313c8.png)

### [2. Knight Rider](https://github.com/RoboticGen/obo-play-sdk/blob/main/digital_output/Knight%20Rider.py)

Lights a series of LEDs in a chase sequence, forward and backward—like the Knight Rider effect.

![4](https://github.com/RoboticGen/obo-play-sdk/blob/main/IMG/415965282-19597621-50a8-4881-a2ed-6499a62c536a.png)


### [3. Push Button](https://github.com/RoboticGen/obo-play-sdk/blob/main/Digital%20Input/Push%20Button.py)
 
Reads a push button using an internal pull-up resistor. Prints “Pressed!” or “Released!” based on the state.
![5](https://github.com/RoboticGen/obo-play-sdk/blob/main/IMG/415965374-8b8864ee-6687-4e04-943f-85e77f092e3b.png)

### [4. Potentiometer](https://github.com/RoboticGen/obo-play-sdk/blob/main/Analog%20Input/Potentiometer.py)

Reads an analog value from a potentiometer using an ADC pin, then prints the raw reading and approximate voltage.

![6](https://github.com/RoboticGen/obo-play-sdk/blob/main/IMG/415965422-2824e2a5-90a2-4907-95b2-461286d202ef.png)

### [5. LED Fade (PWM)](https://github.com/RoboticGen/obo-play-sdk/blob/main/Analog%20Output%20(PWM)/LED%20Fade.py)

Uses PWM to fade an LED in and out by varying the duty cycle on a GPIO pin.
![7](https://github.com/RoboticGen/obo-play-sdk/blob/main/IMG/415965532-6718ed99-dedf-451a-8033-04fd1cc13f75.png)


---

## Notes
- **File Saving**: Replace your "main.py" with the new content ( for ex: blink an LED.py)
- **Pin Assignments**: Adjust pin numbers as needed for your board’s layout or built-in LED.  
- **Timing**: Modify `time.sleep()` calls or loop ranges to speed up or slow down the effects.  
- **Circuit Setup**: Always use current-limiting resistors for LEDs, and wire push buttons or potentiometers correctly (with appropriate pull-ups or pull-downs if needed).  
- **ADC Range**: The ESP32 ADC typically returns values from 0 to 4095 (12-bit resolution). Voltage references can vary; check your board specs.  
- **PWM**: By default in MicroPython, duty cycles range from 0 to 1023 (0–100% duty).

Enjoy exploring these basic MicroPython features on your **OBO-PLAY** ESP32 kit!
