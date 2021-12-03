# A simple sound player
# Plays a loop until it receives a trigger from an ESP32, then plays another sound, then switches back to the loop

import pygame
import time
import serial

# Starting the mixer
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(44100, -16, 2, 1024)

pygame.init()

# play a sound on channel 0
pygame.mixer.Channel(0).play(
    pygame.mixer.Sound('sounds/test.wav'), -1)

trigger = 'FALSE'

# Set up serial reading
ser = serial.Serial()
ser.port = '/dev/cu.usbserial-110'
ser.open()

while True:
    # Parse each input string into array of individual values
    line = ser.readline()
    decoded_line = line[0:len(line)-2].decode("utf-8")
    split_line = decoded_line.split(',')
    trigger = split_line[0]
    print(trigger)

    if trigger == 'TRUE':
        pygame.mixer.Channel(0).play(
            pygame.mixer.Sound('sounds/hello.wav'), -1)
        time.sleep(15)
        pygame.mixer.Channel(0).play(
            pygame.mixer.Sound('sounds/test.wav'), -1)
