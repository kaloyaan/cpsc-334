# A simple stem player / mixer
# You need to download the stems-loop folder as well!

# Joystick controls stem selection
# Button - Solo
# Switch - Mute/Unmute
# There are 4 states - the different tracks playing simultaniously - the button and switch affect different tracks depending on the joystick

import pygame
from gpiozero import Button

# Starting the mixer
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)

pygame.init()

current_song = 1

# play a sound on channel 0
pygame.mixer.Channel(0).play(
    pygame.mixer.Sound('stems/song' + str(current_song) + '/drums.wav'), -1)

# play a sound on channel 1
pygame.mixer.Channel(1).play(
    pygame.mixer.Sound('stems/song' + str(current_song) + '/synth.wav'), -1)

# play a sound on channel 2
pygame.mixer.Channel(2).play(
    pygame.mixer.Sound('stems/song' + str(current_song) + '/vocals.wav'), -1)

# play a sound on channel 3
pygame.mixer.Channel(3).play(
    pygame.mixer.Sound('stems/song' + str(current_song) + '/bass.wav'), -1)

global current_channel
current_channel = 0
prev_volumes = [1, 0, 0, 0]  # init prev_volumes memory for Solo functionality
channel_volumes = [1, 0, 0, 0]  # init set all volumes to max


def update_volumes():
    print("Current volumes: ", channel_volumes)
    for index, volume in enumerate(channel_volumes):
        pygame.mixer.Channel(index).set_volume(volume)


update_volumes()  # init start at 1, 0, 0, 0


# Define buttons
button = Button(2)
switch = Button(19)
joystick_click = Button(21)
joystick_y = Button(20)
joystick_x = Button(16)


def next_channel():
    global current_channel
    if current_channel == 3:
        current_channel = 0
    else:
        current_channel = current_channel + 1
    print("Channel ", current_channel)
    print("Volume ", channel_volumes[current_channel])


def mute_channel():
    # Muting the music
    if channel_volumes[current_channel] == 0:
        print("Unmuted channel ", current_channel)
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
    print("Bye!")
    pygame.mixer.music.stop()
    quit()


def next_song():
    global current_song, current_channel, prev_volumes, channel_volumes
    if current_song == 3:
        current_song = 1
    else:
        current_song += 1

    pygame.mixer.music.stop()
    # Reinitialize
    current_channel = 0
    # init prev_volumes memory for Solo functionality
    prev_volumes = [1, 0, 0, 0]
    channel_volumes = [1, 0, 0, 0]  # init set all volumes to max

    # play a sound on channel 0
    pygame.mixer.Channel(0).play(
        pygame.mixer.Sound('stems/song' + str(current_song) + '/drums.wav'), -1)

    # play a sound on channel 1
    pygame.mixer.Channel(1).play(
        pygame.mixer.Sound('stems/song' + str(current_song) + '/synth.wav'), -1)

    # play a sound on channel 2
    pygame.mixer.Channel(2).play(
        pygame.mixer.Sound('stems/song' + str(current_song) + '/vocals.wav'), -1)

    # play a sound on channel 3
    pygame.mixer.Channel(3).play(
        pygame.mixer.Sound('stems/song' + str(current_song) + '/bass.wav'), -1)

    update_volumes()


print("Flick joystick to select channel, button to solo, switch to mute/unmute. Press joystick to stop")

while True:
    # Joystick X advances channel
    # Joystick Y advances song
    # Only moves forward, cycles once it gets to the end.
    joystick_x.when_pressed = next_channel
    joystick_y.when_pressed = next_song

    # Switch changes mute status - works in both directions for better workflow with joystick
    switch.when_pressed = mute_channel
    switch.when_released = mute_channel

    # Button soloes the current channel
    button.when_pressed = solo_channel
    button.when_released = update_volumes

    # Stop button - joystick click
    joystick_click.when_pressed = stop
