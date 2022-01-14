import datetime
import speakClass
import time

speak_instance = speakClass.speakClass()

class reminderClass:
    def __init__(self):
        self.hour = None
        self.minute = None
        self.tag = None
        pass

    def noteReminder(self, user):
        speak_instance.speakOut("What should I record down?")

        reminder = input("What should I record down?")
        strDate = input("What time?")
        strTime = input("How about date?")

        file = open('Mydata/note.txt', 'a')
        # strDate = datetime.datetime.now().strftime("%d %B %Y")
        file.write(strDate)
        # strTime = datetime.datetime.now().strftime(" %H:%M")
        file.write(strTime)
        file.write(" : ")
        file.write(f'{reminder} recorded by {user} \n')
        speak_instance.speakOut("Done Recording")
    def setAlarm(self):
        # self.hour = input("Tell me the hour you want to set in 24 hour system: ")
        self.minute = int(input("how many the minutes you want to countdown? "))
        self.tag = input("Any reminder? ")
        print(f'Adam: Okay An alarm for {self.minute} is set')
        speak_instance.speakOut(f'An alarm at {self.minute} is set')
        second = self.minute * 60
        print(f'Wake up after {self.minute}. Start Now!')

        time.sleep(second)
        print("RING RING! "+self.tag)
        speak_instance.speakOut("RING RING RING RING RING!")
        speak_instance.speakOut(self.tag)
        self.minute = None
        self.tag = None

    def showReminder(self):
        file = open("Mydata/note.txt", "r")
        file_reminder = file.read()
        print(file_reminder)
        speak_instance.speakOut(file_reminder)
        file.close()

# reminder1 = reminderClass()
# reminder1.noteReminder("JY")
# reminder1.showReminder()