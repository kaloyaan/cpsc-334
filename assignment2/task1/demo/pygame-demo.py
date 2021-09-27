import pygame

# Starting the mixer
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)

pygame.init()

# play a sound on channel 0
pygame.mixer.Channel(0).play(
    pygame.mixer.Sound('stems-2k/drums.wav'))

# play a sound on channel 1
pygame.mixer.Channel(1).play(
    pygame.mixer.Sound("stems-2k/synth.wav"))

# play a sound on channel 2
pygame.mixer.Channel(2).play(
    pygame.mixer.Sound("stems-2k/vocals.wav"))

# play a sound on channel 3
pygame.mixer.Channel(3).play(
    pygame.mixer.Sound("stems-2k/bass.wav"))

# while pygame.mixer.Channel(0).get_busy():
#     pygame.time.Clock().tick(10)

# infinite loop
while True:

    print("Select channel to turn on, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")

    if query == 'p':

        # Muting the music
        pygame.mixer.Channel(0).set_volume(0)
    elif query == 'r':

        # Resuming the music
        pygame.mixer.Channel(0).set_volume(1)
    elif query == 'e':

        # Stop the mixer
        pygame.mixer.music.stop()
        break
