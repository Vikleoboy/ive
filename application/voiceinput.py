# speech to text and text to speech
import speech_recognition as sr


# Function to convert text to speech


def talk():
    # Initialize the recognizer
    r = sr.Recognizer()

    # use the microphone as source for input.

    with sr.Microphone() as source2:
        # wait for a second to let the recognizer
        # adjust the energy threshold based on
        # the surrounding noise level
        r.adjust_for_ambient_noise(source2, duration=0.2)

        # listens for the user's input
        audio2 = r.listen(source2)

        # Using ggogle to recognize audio
        mytext = r.recognize_google(audio2)
        mytext = mytext.lower()
        print(f'u said {mytext}')

        return mytext


def keywords(what_i_said, lst):
    for i in lst:
        if i in what_i_said:
            return True
    return False
