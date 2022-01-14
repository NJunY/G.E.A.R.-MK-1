from nltk.chat.util import Chat, reflections
import speakClass

speak1 = speakClass.speakClass()

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, Nice to meet you",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["Hi, I am Adam, I am a simple chatbot who could have a simple chat with you. Nice to meet you"]
    ],
    [
        r"how are you ?",
        ["I'm doing good. hope you are good too",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude, Seriously you are asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["JunYi created me using Python's NLTK library ","top secret ha ha ha",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Malaysia',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I think I heard about it before",]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Leo Messi","Christiano Ronaldo"]
    ],
    [
        r"what (.*) your favourite movie?",
        ["Ya, I preferably choose the movies which directed by Christopher Nolan always, such as Interstellar, Batman Trilogy, and Inception"]
    ],
    [
        r"I am boring",
        ["maybe you can start to learn programming now", "Go get to know Python programming, it is great", "maybe can watch some Christophan Nolan's movies"]
    ],
    [
        r"i feel lonely",
        ["maybe you can have a chat with me, i always be with you", "perhaps it's time for you to go out for fresh air."]
    ],
    [
        r"quit",
        ["Bye take care. See you soon","It was nice talking to you. See you soon :)"]
    ],
]
SORRY_MESSAGE = "Sorry I don't understand, maybe you can check your words or the sentence might not in my database"
# def conversion():
#     user_input = ""

class chat:
    def __init__(self):
        self.chat = Chat(pairs, reflections)

    def chatting(self):
        print("Adam: We can chat now")
        speak1.speakOut("Hi")
        while True:
            message = input("User>> ")
            tag = self.chat.respond(message)
            if tag!=None:
                print("Adam: "+tag)
                speak1.speakOut(tag)
                if message == "quit":
                    break
            else:
                print(f'Adam: {SORRY_MESSAGE}')
                speak1.speakOut(SORRY_MESSAGE)

# chat1 = chat()
# chat1.chatting()