import cv2
import numpy as np
import speakClass as sc
# import listen

sc_instance = sc.speakClass()

thres = 0.45
nms_threshold = 0.2

tracker = cv2.legacy.TrackerMOSSE_create()

classNames = []
classFile = 'MyFYP/ObjectDetection/coco.names'

with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'MyFYP/ObjectDetection/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'MyFYP/ObjectDetection/frozen_inference_graph.pb'

class ObjectDetection:
    def __init__(self):
        self.net = cv2.dnn_DetectionModel(weightsPath, configPath)
        self.net.setInputSize(320, 320)
        self.net.setInputScale(1.0 / 127.5)
        self.net.setInputMean((127.5, 127.5, 127.5))
        self.net.setInputSwapRB(True)

    def DetectAndShow(self, objects=[]):
        if len(objects) == 0:
            objects = classNames

        cap = cv2.VideoCapture(0)
        # print(objects)
        success, img = cap.read()
        classIds, confs, bbox = self.net.detect(img, confThreshold=thres)
        bbox = list(bbox)
        confs = list(np.array(confs).reshape(1, -1)[0])
        confs = list(map(float, confs))

        indices = cv2.dnn.NMSBoxes(bbox, confs, thres, nms_threshold)

        itemArr = []
        CoorArr = []

        # print(indices)
        for i in indices:
            i = i[0]
            box = bbox[i]
            try:
                if objects[0] == classNames[classIds[i][0] - 1]:
                    detectedObject = objects[classIds[i][0] - 1]
                    itemArr.append(detectedObject)
                    x, y, w, h = box[0], box[1], box[2], box[3]
                    CoorArr.append((x, y, w, h))
            except:
                pass
            # cv2.rectangle(img, (x, y), (x + w, h + y), color=(0, 255, 0), thickness=1)
            # cv2.putText(img, detectedObject, (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_SIMPLEX,
            #             1, (0, 255, 0), 2)

        result = {
            "foundItem": itemArr,
            "foundCoordinate": CoorArr,
            # "frame": img
        }

        cap.release()

        return result

    def getCenter(self, bbox):
        x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
        endpointX = x + w
        endpointY = y + h
        centerX = (x + endpointX) // 2  # (x1+x2)/2
        centerY = (y + endpointY) // 2  # (y1+y2)/2 Midpoint formula
        return [centerY, centerX]

    def drawBox(self, img, bbox, object):
        x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
        cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 3)
        centerY, centerX = ObjectDetection.getCenter(self, bbox)
        # print((centerY,centerX))
        cv2.circle(img, (centerX, centerY), radius=2, color=(255,0,255), thickness=1)
        cv2.putText(img, f'Tracking {object}', (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    def ObjectTrack(self, object):
        # l = listen.listen()
        # cap = cv2.VideoCapture(0)
        result = ObjectDetection.DetectAndShow(self, objects=[object])
        print(result["foundItem"])
        # print(len(result["foundItem"]))
        cap = cv2.VideoCapture(0)
        if len(result["foundItem"]) == 1:
            bbox = result["foundCoordinate"][0]
            # print(bbox)
            success, frame = cap.read()
            # bbox = cv2.selectROI("Tracking", frame, False)
            tracker.init(frame, bbox)
            # print(bbox)
            X_prev = int(bbox[0])
            while True:
                timer = cv2.getTickCount()
                success, img = cap.read()
                success, bbox = tracker.update(img)
                # print(img.shape)

                centerX, centerY = ObjectDetection.getCenter(self, bbox)
                maxHeight, maxWidth, ColourChannel = img.shape
                if success:
                    if (centerX>=0 and centerX<=maxWidth) and (centerY>=0 and centerY<=maxHeight):
                        ObjectDetection.drawBox(self, img, bbox, object)
                    else:
                        cap.release()
                        cv2.destroyAllWindows()
                        sc_instance.speakOut('Target Lost')
                        break
                else:
                    cap.release()
                    cv2.destroyAllWindows()
                    sc_instance.speakOut('Target Lost')
                    break

                cv2.rectangle(img, (15,15), (200,90), (255,0,255),2)
                cv2.putText(img, "FPS: ", (20,40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,255), 2)
                cv2.putText(img, "Status: ", (20,75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,255), 2)

                # cv2.line(img, (0,0), (25,25), (255,0,255), 2)
                X = int(bbox[0])
                if X == X_prev:
                    flow = "Same"
                elif X > X_prev:
                    flow = "Left"
                elif X < X_prev:
                    flow = "Right"
                # print(flow)
                cv2.putText(img, f'X: {flow}', (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,255), 1)
                X_prev = X

                fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
                if fps > 60:
                    myColor = (20, 230, 20)
                elif fps > 20:
                    myColor = (230, 20, 20)
                else:
                    myColor = (20, 20, 230)

                cv2.putText(img, str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, myColor, 2);

                cv2.imshow("Tracking", img)

                if cv2.waitKey(1) & 0xff == ord('q'):
                    cap.release()
                    cv2.destroyAllWindows()
                    break
        else:
            cap.release()
            sc_instance.speakOut(f'Sorry, I didnt find {object}')

