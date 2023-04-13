import pygame


class pitkula(pygame.sprite.Sprite):
    def __init__(self, korkeus, leveys):
        super().__init__()
        self.color = (0, 191, 255)
        self.rect = pygame.Rect(0,0,30,30)
        # mitat on 1x4
        self.muoto = [[1], [1], [1], [1]]
