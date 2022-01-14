import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 130)

class speakClass:
    def __init__(self):
        pass

    def speakOut(self, speech):
        # print(speech)
        engine.say(speech)

        engine.runAndWait()
        
# speak1 = speakClass()
# speak1.speakOut("Ho There hi there hi there")