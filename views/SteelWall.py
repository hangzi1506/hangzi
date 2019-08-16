import  pygame
class SteelWall:
    def __init__(self,x,y,window):
        self.x=x
        self.y =y
        self.window= window
        self.image=pygame.image.load('./img/steels.gif')


    def display(self):
        self.window.blit(self.image,(self.x,self.y))