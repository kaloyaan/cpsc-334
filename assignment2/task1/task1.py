# A simple stem player / mixer
# Joystick controls stem selection
#Button - Solo
#Switch - Mute/Unmute

import pygame
from gpiozero import Button

# Starting the mixer
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)

pygame.init()

# play a sound on channel 0
pygame.mixer.Channel(0).play(
    pygame.mixer.Sound('stems-loop/drums.wav'), -1)

# play a sound on channel 1
pygame.mixer.Channel(1).play(
    pygame.mixer.Sound("stems-loop/synth.wav"), -1)

# play a sound on channel 2
pygame.mixer.Channel(2).play(
    pygame.mixer.Sound("stems-loop/vocals.wav"), -1)

# play a sound on channel 3
pygame.mixer.Channel(3).play(
    pygame.mixer.Sound("stems-loop/bass.wav"), -1)

# Define buttons
button = Button(2)
switch = Button(19)
joystick_click = Button(21)
joystick_y = Button(20)
joystick_x = Button(16)

global current_channel
current_channel = 0
prev_volumes = [1, 1, 1, 1]  # init prev_volumes memory for Solo functionality
channel_volumes = [1, 1, 1, 1]  # init set all volumes to max


def next_channel():
    global current_channel
    if current_channel == 3:
        current_channel = 0
    else:
        current_channel = current_channel + 1
    print("Channel ", current_channel)
    print("Volume ", channel_volumes[current_channel])


def update_volumes():
    print("Current volumes: ", channel_volumes)
    for index, volume in enumerate(channel_volumes):
        pygame.mixer.Channel(index).set_volume(volume)


def mute_channel():
    # Muting the music
    if channel_volumes[current_channel] == 0:
        print("Unuted channel ", current_channel)
        channel_volumes[current_channel] = 1
    else:
        print("Muted channel ", current_channel)
        channel_volumes[current_channel] = 0

    update_volumes()


def solo_channel():
    # Solo channel - only on hold
    # Turn all channels off except current_channel
    print("Soloed channel ", current_channel)
    for index, volume in enumerate(channel_volumes):
        if index == current_channel:
            pygame.mixer.Channel(index).set_volume(1)
        else:
            pygame.mixer.Channel(index).set_volume(0)


def stop():
    pygame.mixer.music.stop()
    quit()


print("Flick joystick to select channel, button to solo, switch to mute/unmute. Press joystick to stop")

while True:
    # Joystick advances channel
    joystick_x.when_pressed = next_channel
    joystick_y.when_pressed = next_channel

    # Switch changes mute status
    switch.when_pressed = mute_channel
    switch.when_released = mute_channel

    # Button solos
    button.when_held = solo_channel
    button.when_released = update_volumes

    joystick_click.when_pressed = stop
