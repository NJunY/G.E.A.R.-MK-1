import pygame
import driving

drive1 = driving.Drive(2,3,4,17,27,22)

class driveControl():
    def __init__(self):
        pass

    def getKey(self, keyName):
        ans = False
        for eve in pygame.event.get(): pass
        keyInput = pygame.key.get_pressed()
        myKey = getattr(pygame, 'K_{}'.format(keyName))
        if keyInput[myKey]:
            ans = True
        pygame.display.update()

        return ans

    def mainDrive(self):
        pygame.init()
        win = pygame.display.set_mode((10,10))
        while True:
            if self.getKey('UP'):
                drive1.move(0.7, 0, 0.1)
            elif self.getKey('DOWN'):
                drive1.move(-1, 0, 0.1)
            elif self.getKey('LEFT'):
                # print('Key Left was pressed')
                drive1.move(0.5, -0.3, 0.1)
            elif self.getKey('RIGHT'):
                # print('Key Right was pressed')
                drive1.move(0.5, 0.3, 0.1)
            elif self.getKey('q'):
                pygame.quit()
                # exit()
                break
            else:
                drive1.stop()

# control1 = driveControl()
# control1.mainDrive()