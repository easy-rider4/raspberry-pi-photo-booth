# Photo-booth

This is the code for a Raspberry Pi photo-booth in python.

## Hardware
- Raspberry Pi 2 Model B
- Pi Camera
- Jump wires and buttons
- T-Cobbler for Raspberry Pi 2
- SD-Card
- USB-Hub
- Wlan-adapter
- HDMI Display
- HDMI cable


## Software
- Raspbian
- Python
- picamera
- gpio


## Installation
todo


## Run
1. config.py
USB_PATH = set if usb-device is used for storage
NUMBER_OF_PICTURES = number of pictures that should be taken
INTERVAL_IN_SECONDS = length of the countdown between shooting pics


2. if usb is used
format = FAT 
name = PHOTOBOOTH


3. make sure you are in the directory /home/pi/pi-photo-booth and run
./start-booth-usb.sh or
./start-booth.sh

4. when finished run
./remove-usb.sh

