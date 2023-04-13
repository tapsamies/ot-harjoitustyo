import pygame


class l_pala(pygame.sprite.Sprite):
    def __init__(self, korkeus,leveys):
        super().__init__()

        self.color = (255, 165, 0)
        self.rect = pygame.Rect(0,0,30,30)
        # korkeus vaakatasossa: 1,1,2
        self.muoto = [[1, 0],
                      [1, 0],
                      [1, 1]]
