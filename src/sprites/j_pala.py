import pygame


class j_pala(pygame.sprite.Sprite):
    def __init__(self, korkeus, leveys):
        super().__init__()

        self.color = (0, 0, 139)
        self.rect = pygame.Rect(0,0,30,30)
        # mitat on 2,1,1
        self.muoto = [[0, 1],
                      [0, 1],
                      [1, 1]]
