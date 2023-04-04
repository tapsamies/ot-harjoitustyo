import pygame

class pitkula(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.color = (0,191,255)
        self.rect.x = x
        self.rect.y = y
        #mitat on 1x4
        self.muoto = [[1],[1],[1],[1]]

