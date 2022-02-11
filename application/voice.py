# imports
import gtts
from playsound import playsound
import os

# function with say's stuff when we give text and save it as hello.mp3 and then play it
def say(text):
    try:
        text = gtts.gTTS(text)
        text.save('hello.mp3')
        playsound('hello.mp3')
        os.remove('hello.mp3')
    except:
        pass

