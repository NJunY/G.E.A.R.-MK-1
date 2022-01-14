import cv2
import os

import speakClass
# import listen

cascPath = 'Mydata/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

class register:
    def __init__(self):
        pass

    def registerUser(self):
        # detect face
        cam = cv2.VideoCapture(0)

        ret, frame = cam.read()
        cv2.imshow("test", frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

        if len(faces) == 1:
            # for (x, y, w, h) in faces:
            #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # read message
            speak_instance = speakClass.speakClass()
            speak_instance.speakOut("please tell me your name")

            # user_name = "sorry i don't the get idea"
            # listen name
            # listen_instance = listen.listen()
            # listen_result = listen_instance.listenTo()
            listen_result = input("please tell me your name")
            if "cancel" in listen_result:
                speak_instance.speakOut("No problem")
                return
            # while listen_result == user_name:
            #     speak_instance.speakOut("Sorry please tell me again")
            #     listen_result = listen_instance.listenTo()
            #
            #     if "cancel" in listen_result:
            #         speak_instance.speakOut("No problem")
            #         break

            # if listen_result != user_name:
            user_name = listen_result
            img_name = "{}.jpg".format(user_name)
            path = 'userImage'
            cv2.imwrite(os.path.join(path, img_name), frame)
            print("Register complete")
            speak_instance.speakOut("registered Complete")

        elif len(faces) > 1:
            print("too many faces, ONLY one face is allowed!")
        elif len(faces) < 1:
            print("Can't detect any face")

        cam.release()
        cv2.destroyAllWindows()

# regist = register()
# regist.registerUser()
