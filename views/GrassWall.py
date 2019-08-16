import  pygame
class GrassWall:
    def __init__(self,x,y,window):
        self.x=x
        self.y =y
        self.window= window
        self.image=pygame.image.load('./img/grass.png')


    def display(self):
        self.window.blit(self.image,(self.x,self.y))