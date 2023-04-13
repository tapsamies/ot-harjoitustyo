import pygame


class z_pala(pygame.sprite.Sprite):
    def __init__(self, leveys, korkeus):
        super().__init__()

        self.color = (255, 0, 0)
        self.rect = pygame.Rect(0,0,30,30)
        # mitat on 1,2,1
        self.muoto = [[1, 1, 0],
                      [0, 1, 1]]
