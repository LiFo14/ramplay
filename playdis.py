import pygame, time
from random import randint

class PlayDis:
    def __init__(self, n):
        print "Playing " + n

    def initSeq(self, s):
        s = list(s)
        for x in s:
            if x == '9' or x == '0':
                x = randint(1,8)
            self.playSeq(x)

    def playSeq(self, sq):
        path = '/home/nikita/Dropbox/Python/Code/ramplay/mus/' + str(sq) + '.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        time.sleep(0.9)
        pygame.mixer.music.stop()

if __name__ == '__main__':
    pd = PlayDis()
    #pd.playSeq(1)
    pos = (1,2,3,4,5,6,7,8)
    for s in pos:
        pd.playSeq(s)
