import json
import random

class ReturnResponse:
    def __init__(self):
        json_file = open('Mydata/content.json')
        content = json.load(json_file)
        json_file.close()
        self.response = content['intents']

    def registerResponse(self):
        return self.response[8]['responses'][random.randint(0,6)]

    def recognizeResponse(self):
        return self.response[7]['responses'][random.randint(0, 6)]

    def detectionResponse(self):
        return self.response[6]['responses'][random.randint(0,6)]

    def trackResponse(self):
        return self.response[5]['responses'][random.randint(0,5)]

    def driveResponse(self):
        return self.response[4]['responses'][random.randint(0,4)]

# r1 = ReturnResponse()
# print(r1.registerResponse())
# print(r1.recognizeResponse())
# print(r1.detectionResponse())
# print(r1.trackResponse())
# print(r1.driveResponse())