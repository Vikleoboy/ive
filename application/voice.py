# imports
import gtts
from playsound import playsound


# function with say's stuff when we give text and save it as hello.mp3 and then play it
def say(text):
    try:
        text = gtts.gTTS(text)
        text.save('hello.mp4')
        playsound('hello.mp4')
    except:
        pass

say('ok')