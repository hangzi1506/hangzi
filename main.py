import pygame
from pygame.locals import *
from util.local import*
import sys

def start():
    pygame.init()
    window=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("坦克大战")
    #加载大本营
    iconImage=pygame.image.load('./img/camp.gif')
    pygame.display.set_icon(iconImage)
    while True:
        #xianshi

        eventList=pygame.event.get()
        for eventEle in eventList:
            if eventEle.type==QUIT:
                pygame.quit()
                sys.exit()
if __name__=='__main__':
    start()