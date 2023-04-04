import pygame

class t_pala(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.color = (255,0,255)
        self.rect.x= x
        self.rect.y = y
        #mitat on 1,2,1
        self.muoto= [[1,1,1],
                     [0,1,0]]
