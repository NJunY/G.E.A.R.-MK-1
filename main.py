import speakClass
# import listen
# import chat_tf
import registerUser
import answering
import recognizeUser
import obde
import reminderAlarm
import chat_nltk
import userHelp
import ReturnResponse
import driveControl

import time

drive_istance = driveControl.driveControl()
speak_instance = speakClass.speakClass()
answer_instance = answering.answering()
# recognize_instance = recognizeUser.recognize()
objectDe_instance = obde.ObjectDetection()
chat_instance = chat_nltk.chat()
help_instance = userHelp.help()
r_instance = reminderAlarm.reminderClass()
response_instance = ReturnResponse.ReturnResponse()

recognized_user = None
ERROR_MESSAGE = "Sorry I dont understand, maybe you may try with other word"

def respondMessage(message):
    print("Adam: "+message)
    speak_instance.speakOut(message)

def findingUser():
    recognize_instance = recognizeUser.recognize()
    foundUser = recognize_instance.recognizeFace()
    if foundUser == "1":
        speak_instance.speakOut('Too many person, only one is allowed at the same time')
        return None
    elif foundUser == "0":
        speak_instance.speakOut('No Human Face is found')
        return None
    elif foundUser == "-1":
        speak_instance.speakOut("There is no Registered User")
        return None
    else:
        speak_instance.speakOut('Hi, nice to meet you '+foundUser)
        return foundUser

while True:
    speak_instance.speakOut("I am ready")
    print("Type help to get assistance")
    typing_result = input("USER>> ")
    if "question" in typing_result:
        speak_instance.speakOut("What is your question?")
        question = input("What is your question?")
        result = answer_instance.answerQuestion(question)
        print(result)
        speak_instance.speakOut(result)
    elif "show reminder" in typing_result:
        r_instance.showReminder()
    elif "reminder" in typing_result:
        if (recognized_user!=None):
            r_instance.noteReminder(recognized_user)
        else:
            speak_instance.speakOut("Please type recognize and let me recognize you first")
            # speak_instance.speakOut("Please let me recognize your face first. put your face at the front of the camera now.")
            # time.sleep(2)
            # findingUser()
            # if recognized_user==None:
            #     speak_instance.speakOut("Sorry, no user is found")
            # else:
            #     r_instance = reminderAlarm.reminderClass()
            #     r_instance.noteReminder()
    elif "alarm" in typing_result:
        r_instance.setAlarm()
    elif "help" in typing_result or "user manual" in typing_result:
        help_instance.helpManual()
    elif "register" in typing_result:
        msg = response_instance.registerResponse()
        respondMessage(msg)
        register_instance = registerUser.register()
        register_instance.registerUser()
    elif "recognize" in typing_result:
        msg = response_instance.recognizeResponse()
        respondMessage(msg)
        recognized_user = findingUser()
    elif "detection" in typing_result:
        msg = response_instance.detectionResponse()
        respondMessage(msg)
        result = objectDe_instance.DetectAndShow()
        foundObject = result['foundItem']
        print(foundObject)
        if len(foundObject)==0:
            speak_instance.speakOut("Nothing found")
        else:
            speak_instance.speakOut(foundObject)
    elif "track" in typing_result or "tracking" in typing_result:
        speak_instance.speakOut("Please tell me the object you want to track")
        target = input("Please tell me the object you want to track: ")
        objectDe_instance.ObjectTrack(target)
    elif "drive" in typing_result:
        msg = response_instance.driveResponse()
        respondMessage(msg)
        drive_istance.mainDrive()
        # objectDe_instance.ObjectTrack()
    elif "chat" in typing_result:
        chat_instance.chatting()
    elif "clear" in typing_result:
        recognized_user = None
        respondMessage("Recognized user cleared")
    else:
        print(ERROR_MESSAGE)
        speak_instance.speakOut(ERROR_MESSAGE)
    # else:
    #     chat_instance = chat.chat()
    #     # get predicted chat tag
    #     predicted_tag = chat_instance.getTag(typing_result)
    #     # get reply from program
    #     predicted_reply = chat_instance.getReply(predicted_tag)
    #
    #     speak_instance.speakOut(predicted_reply)
    #
    #     if predicted_tag == "goodbye":
    #         break
    #     elif predicted_tag == "register":
    #         register_instance = registerUser.register()
    #         register_instance.registerUser()
    #     elif predicted_tag == "recognize":
    #         findingUser()
    #     elif predicted_tag == "detection":
    #         result = objectDe_instance.DetectAndShow()
    #         foundObject = result['foundItem']
    #         speak_instance.speakOut(foundObject)
    #     elif predicted_tag == "drive":
    #         objectDe_instance.ObjectTrack()
    time.sleep(0.5)