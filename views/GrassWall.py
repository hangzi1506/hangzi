import  pygame
from base.View import*
class GrassWall(View):
    def __init__(self,**kwargs):
        super(GrassWall, self).__init__(**kwargs,img='./img/grass.png')
        # self.x=x
        # self.y =y
        # self.window= window
        # self.image=pygame.image.load('./img/grass.png')


    # def display(self):
    #     self.window.blit(self.image,(self.x,self.y))