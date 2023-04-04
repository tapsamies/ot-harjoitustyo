import pygame

class j_pala(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.color = (0,0,139)
        self.rect.x= x
        self.rect.y = y
        #mitat on 2,1,1
        self.muoto=[[0,1],
                    [0,1],
                    [1,1]]

