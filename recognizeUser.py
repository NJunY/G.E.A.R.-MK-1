import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'userImage'
# images = []
classNames = []
myList = os.listdir(path)

class recognize:
    def __init__(self):
        images = []
        classNames = []
        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])
        print(classNames)
        self.encodeList = []
        i = 0
        # if len(images)==0:
        #     return
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            try:
                encode = face_recognition.face_encodings(img)[0]
            except:
                print(f'There is no face can be found in image of {classNames[i]}')
            self.encodeList.append(encode)
            i += 1
        # if len(self.encodeList)==0:
        #     return "-1"
        print("Done")

    def recordLoginHistory(self, name):
        with open('LoginHistory.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')

    def recognizeFace(self):
        if len(self.encodeList)==0:
            return "0"
        cap = cv2.VideoCapture(0)
        success, img = cap.read()
        imgS = cv2.resize(img, (0,0), None, 0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        cap.release()

        nameList = []
        for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(self.encodeList, encodeFace)
            faceDis = face_recognition.face_distance(self.encodeList, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                self.recordLoginHistory(name)
                nameList.append(name)

        if len(nameList) == 1:
            return nameList[0]
        elif len(nameList) > 1:
            return "1"
        elif len(nameList) == 0:
            return "0"

# r = recognize()
# print(r.recognizeFace())
