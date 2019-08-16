
import  pygame
from base.View import*
class HeroTank(View):
    def __init__(self,**kwargs):
        super(HeroTank, self).__init__(**kwargs,img='./img/p1tankU.gif')
        
    # def __init__(self,x,y,window):
        # self.x=x
        # self.y =y
        # self.window= window
        # self.image=pygame.image.load('./img/p1tankU.gif')


    # def display(self):
    #     self.window.blit(self.image,(self.x,self.y))
