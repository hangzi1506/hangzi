import  pygame
from base.View import *
class WaterWall(View):
    def __init__(self,**kwargs):
        super(WaterWall, self).__init__(**kwargs,img='./img/water.gif')
    # def __init__(self,x,y,window):
    #     self.x=x
    #     self.y =y
    #     self.window= window
    #     self.image=pygame.image.load('./img/water.gif')


    # def display(self):
    #     self.window.blit(self.image,(self.x,self.y))