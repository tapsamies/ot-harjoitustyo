import pygame

class l_pala(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.color = (255,165,0)
        self.rect.x= x
        self.rect.y = y
        #korkeus vaakatasossa: 1,1,2
        self.muoto= [[1,0],
                     [1,0],
                     [1,1]]
