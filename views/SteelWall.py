import  pygame
from base.View import *
class SteelWall(View):
    def __init__(self,**kwargs):
        super(SteelWall, self).__init__(**kwargs,img='./img/steels.gif')
    #     self.x=x
    #     self.y =y
    #     self.window= window
    #     self.image=pygame.image.load('./img/steels.gif')
    #
    #
    # def display(self):
    #     self.window.blit(self.image,(self.x,self.y))