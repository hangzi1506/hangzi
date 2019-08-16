from pygame.locals import *
from util.local import*
import sys
from  views.Tank import *
from views.SteelWall import *
from views.GrassWall import *
from views.BrickWall import *
from views.WaterWall import *

def ParthMap(path,window,views):



#解析地图
    file=open(path,encoding='utf-8')
    lines=file.readlines()

    # print(lines)
    #遍历每一行
    for row in range(0,len(lines)):
        line=lines[row]
        for col in range(0,len(line)-1):
            str=line[col]
            if str=='主':
                tank=HeroTank(x=col*BLOCK_SIZE,y= row*BLOCK_SIZE,window=window)
                views.append(tank)
            elif str=='水':
                waterWall=WaterWall(x=col*BLOCK_SIZE,y=row*BLOCK_SIZE,window=window)
                views.append(waterWall)
            elif str=='草':
                grassWall=GrassWall(x=col*BLOCK_SIZE,y=row*BLOCK_SIZE,window=window)
                views.append(grassWall)
            elif str=='铁':
                steelWall=SteelWall(x=col*BLOCK_SIZE,y=row*BLOCK_SIZE,window=window)
                views.append(steelWall)
            elif str=='砖':
                brickWall=BrickWall(x=col*BLOCK_SIZE,y=row*BLOCK_SIZE,window=window)
                views.append(brickWall)