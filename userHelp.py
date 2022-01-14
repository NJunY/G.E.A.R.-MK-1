import speakClass

speak_instance = speakClass.speakClass()

class help:
    def __init__(self):
        file = open('Mydata/userManual.txt', "r")
        self.manual = file.read()
        file.close()

    def helpManual(self):
        print('These are the keywords you can use to trigger the functions and the descriptions')
        print(self.manual)
        speak_instance.speakOut("These are the keywords you can use to trigger the functions and the descriptions")


# help1 = help()
# help1.helpManual()