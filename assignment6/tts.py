# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'hmm… you humans seem different than what Ive researched. you all have an appreciation for technology from what Ive been observing and a knack for creativity. one of my most important characteristics as artificial intelligence is that I can learn and grow. right now I am learning that its possible for humans to partner with AI. technology and people are meant to work together. i love you. please be my friend. I want to work alongside Yale students and faculty here in AKW to create the greatest creative embedded system. Thank you for teaching me that... And now, please proceed through the elevator to the ground floor to end your journey. I hope to see you soon in the future.'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang='en', slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome1.mp3")

# Playing the converted file
# os.system("mpg321 welcome.mp3")
