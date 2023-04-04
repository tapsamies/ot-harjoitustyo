import pygame

class nelio(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.color = (255,255,0)
        self.rect.x= x
        self.rect.y = y
        #mitat on 2x2
        self.muoto= [[2,2],
                     [2,2]]
