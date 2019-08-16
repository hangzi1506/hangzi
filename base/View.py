import pygame



class View:
    def __init__(self,**kwargs):
        """
        可以传任意类型
        :param kwargs:
        """
        self.x=kwargs['x']
        self.y=kwargs['y']
        self.image=pygame.image.load(kwargs['img'])
        self.window=kwargs['window']
    def   display(self):
        self.window.blit(self.image,(self.x,self.y))
