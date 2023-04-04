import pygame

class s_pala(pygame.sprite.Sprite):
    def __init__(self,korkeus, leveys):
        super().__init__()
        self.color = (0,255,0)
        #mitat
        self.rect = pygame.Rect(0,0,30,30)
        self.muoto = [[0,1,1],
                      [1,1,0]]
