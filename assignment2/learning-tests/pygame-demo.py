import pygame

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

# while pygame.mixer.Channel(0).get_busy():
#     pygame.time.Clock().tick(10)

current_channel = 0
prev_volumes = [1, 1, 1, 1]
channel_volumes = [1, 1, 1, 1]


def change_channel(channel):
    if channel == 3:
        return(0)
    else:
        return(channel + 1)


# infinite loop
while True:

    print("Press A to select channel, S to solo, D to mute/unmute")
    print("Press 'e' to exit the program")
    query = input("  ")

    if query == 'd':
        # Muting the music
        if channel_volumes[current_channel] == 0:
            channel_volumes[current_channel] = 1
        else:
            channel_volumes[current_channel] = 0

        pygame.mixer.Channel(current_channel).set_volume(
            channel_volumes[current_channel])

    elif query == 'a':

        # Change channel
        current_channel = change_channel(current_channel)
        print("Current channel: ", current_channel)

    elif query == 's':

        # Solo channel - only on hold
        # Save previous channel config
        # Turn all channels off except current_channel
        # Upon release restore previous config
        print("TODO")

    elif query == 'e':

        # Stop the mixer
        pygame.mixer.music.stop()
        break
