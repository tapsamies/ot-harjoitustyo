import pygame


class nelio(pygame.sprite.Sprite):
    def __init__(self, korkeus, leveys):
        super().__init__()

        self.color = (255, 255, 0)
        self.rect = pygame.Rect(0,0,30,30)
        # mitat on 2x2
        self.muoto = [[2, 2],
                      [2, 2]]
