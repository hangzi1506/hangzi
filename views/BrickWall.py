import  pygame
from base.View import *
class BrickWall(View):
    def __init__(self,**kwargs):
        super(BrickWall, self).__init__(**kwargs,img='./img/walls.gif')
    #     self.x=x
    #     self.y =y
    #     self.window= window
    #     self.image=pygame.image.load('./img/walls.gif')
    #
    #
    # def display(self):
    #     self.window.blit(self.image,(self.x,self.y))