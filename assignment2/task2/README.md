# CPSC 334 Assignment #2 - Kalo's Stem Player

*Kalo's Stem Player* is a simple stem player device. It can play 4 different song parts: drums, guitar/synth, bass and vocals. You can mute and unmute them using the switch, and solo just the one you're on using the button. The joystick controls the stem and song selection. There's 3 songs loaded on there right now!

![Box](readme-images/box.png)

![Diagram](readme-images/diagram.png)

## Video demo

Check it out: [https://www.youtube.com/watch?v=ghRyUcrA4c8](https://www.youtube.com/watch?v=ghRyUcrA4c8)


## Run Mode 1:

Using only the Raspberry Pi GPIO.

1. Connect switch, button and joystick to Raspberry Pi GPIO
2. Specify the pins you've connected it to in the `stem-player.py` variables
3. Connect Raspberry Pi to power and speaker to 3.5mm jack or Bluetooth
4. Run code - `stem-player.py` and perform!
5. For a gentle shutdown, click the joystick button. Or just Ctrl+C.

## Run Mode 2:

Using ESP32 and Raspberry Pi/some other computer.

*ESP32 here functions as an input parser, while the Pi as just the audio generator.*

1. Connect switch, button and joystick to ESP32 with `esp32-serial` code uploaded
2. Connect ESP32 to Raspberry Pi using USB cable. You can put the Pi in the box or take it out if you have a long USB cable.
3. Connect Raspberry Pi to power and speaker to 3.5mm jack or Bluetooth
4. Run code and perform!
5. For a gentle shutdown, click the joystick button. Or just Ctrl+C.
