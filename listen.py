import speech_recognition as sr

r = sr.Recognizer()

class listen:

    def __init__(self):
        pass

    def listenTo(self):
        with sr.Microphone() as mic:
            print("ready")
            r.adjust_for_ambient_noise(mic, duration=0.2)
            audio = r.listen(mic)
            print("recognizing...")

            try:
                text = r.recognize_google(audio)
                # text = text.lower()
                print(text)

                return text
            except:
                print("sorry i dont get the idea")
                return "sorry i dont the get idea"