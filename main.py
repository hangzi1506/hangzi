import pygame
from pygame.locals import *
from util.local import*
import sys
from  views.Tank import *
from views.SteelWall import *
from views.GrassWall import *
from views.BrickWall import *
from views.WaterWall import *

def start():
    pygame.init()
    window=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("坦克大战")
    #加载大本营
    iconImage=pygame.image.load('./img/camp.gif')
    pygame.display.set_icon(iconImage)

    # TankImage=pygame.image.load('./img/p1tankU.gif')
    tank=HeroTank(x=100,y=100,window=window)
    brickWall=BrickWall(x=160,y=160,window=window)
    grassWall=GrassWall(x=220,y=220,window=window)
    steelWall = SteelWall(x=280,y= 280,window= window)
    waterWall = WaterWall(x=340, y=340,window= window)

    while True:
        #xianshi
        tank.display()
        brickWall.display()
        grassWall.display()
        steelWall.display()
        waterWall.display()


        pygame.display.flip()

        # window.blit(TankImage,(300,300))
        pygame.display.flip()
        eventList=pygame.event.get()
        for eventEle in eventList:
            if eventEle.type==QUIT:
                pygame.quit()
                sys.exit()
if __name__=='__main__':
    start()