import pygame


class Lpala(pygame.surface.Surface):
    def __init__(self, koko):
        # super().__init__((30, 30))
        self.color = (255, 165, 0)
        self.rect = pygame.surface.Surface((koko, koko))
        self.muoto = [(2*koko, 0),
                      (3*koko, 0),
                      (koko, 0),
                      (koko, koko)]
        # for i in self.muoto:
        super().__init__((koko, koko))
        super().fill(self.color)


class Ipala(pygame.surface.Surface):
    def __init__(self, koko):
        # super().__init__((30,30))
        self.color = (0, 191, 255)
        self.rect = pygame.surface.Surface((koko, koko))
        self.muoto = [[1, 0],
                      [1, 0],
                      [1, 0],
                      [1, 0]]
        super().__init__((koko*4, koko))
        super().fill((self.color))


class Spala(pygame.surface.Surface):
    def __init__(self, koko):
        super().__init__((30, 30))
        self.color = (0, 255, 0)
        self.rect = pygame.surface.Surface((koko, koko))
        self.muoto = [[1, 0],
                      [1, 1],
                      [0, 1]]


class Zpala(pygame.surface.Surface):
    def __init__(self, koko):
        super().__init__((30, 30))
        self.color = (255, 0, 0)
        self.rect = pygame.surface.Surface((koko, koko))
        self.muoto = [[0, 1],
                      [1, 1],
                      [1, 0]]


class Jpala(pygame.surface.Surface):
    def __init__(self, koko):
        super().__init__((30, 30))
        self.color = (0, 0, 139)
        self.rect = pygame.surface.Surface((koko, koko))
        self.muoto = [[0, 1],
                      [0, 1],
                      [1, 1]]


class Npala(pygame.surface.Surface):
    def __init__(self, koko):
        super().__init__((30, 30))
        self.color = (255, 255, 0)
        self.rect = pygame.surface.Surface((koko, koko))
        self.muoto = [[2, 2],
                      [2, 2]]


class Tpala(pygame.surface.Surface):
    def __init__(self, koko):
        super().__init__((30, 30))
        self.color = (255, 0, 255)
        self.rect = pygame.surface.Surface((koko, koko))
        self.muoto = [[1, 1, 1],
                      [0, 1, 0]]
