import pygame
from pygame.locals import *
from util.local import*
import sys
from  views.Tank import *
from views.SteelWall import *
from views.GrassWall import *
from views.BrickWall import *
from views.WaterWall import *
from util.parth import *


views=[]
def start():
    pygame.init()
    window=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("坦克大战")
    #加载大本营
    iconImage=pygame.image.load('./img/camp.gif')
    pygame.display.set_icon(iconImage)


    #加载地图
    ParthMap('./map/1.map',window,views)






    #




    while True:
        #xianshi
        # tank.display()
        # brickWall.display()
        # grassWall.display()
        # steelWall.display()
        # waterWall.display()

        for view in views:
            view.display()
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