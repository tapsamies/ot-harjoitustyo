import pygame


class t_pala(pygame.sprite.Sprite):
    def __init__(self, korkeus,leveys):
        super().__init__()

        self.color = (255, 0, 255)
        self.rect = pygame.Rect(0,0,30,30)
        # mitat on 1,2,1
        self.muoto = [[1, 1, 1],
                      [0, 1, 0]]
