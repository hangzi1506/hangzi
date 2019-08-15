import pygame
from pygame.locals import *
from util.local import*
import sys

def start():
    pygame.init()
    window=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

    while True:
        eventList=pygame.event.get()
        for eventEle in eventList:
            if eventEle.type==QUIT:
                pygame.quit()
                sys.exit()
if __name__=='__main__':
    start()