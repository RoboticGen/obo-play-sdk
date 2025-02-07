# OBO-Play SDK Documentation
<p align="center">

<img width="100%" src="https://github.com/user-attachments/assets/b8f67c37-569a-48df-81a6-ba8012133346" text="OBO PLAY">
  <p align="center">
    </p> 

---
This repository provides sample code and documentation for the **Obo-Play Kit** – a MicroPython-based kit featuring an ESP32, a half breadboard, and an SSD1306 OLED display. You’ll find:

- A library (`oboplay.py`) to initialize and control the OLED display.
- A standalone Night-rider demo (`nightrider.py`).

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

3. **Upload the OBOCar SDK**:
   - Create a new file in Thonny.
   - Copy the contents of `obocar.py` into the file.
   - Click Save
   - Select 'Micropython device'
   - Rename as `obocar.py`
   - Select OK
  
3. **Upload the Test Code**:
   - Create a new file in Thonny.
   - Copy the contents of `boot.py` into the file.
   - Click Save
   - Select 'Micropython device'
   - Rename as `boot.py`
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

With these steps, you should be able to regain control of your ESP32 and continue using the OBOCar SDK.


Happy coding with your Obo-Play Kit!
