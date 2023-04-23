import pygame



class Lpala(pygame.surface.Surface):
    def __init__(self, koko):
        self.color = (255, 165, 0)
        self.rect = pygame.surface.Surface((koko, koko))
        self.muoto = [[2*koko, 1],
                      [3*koko, 1],
                      [koko, 1],
                      [koko, koko]]
        super().__init__((koko, koko))
        super().blit(self.rect,(0,0))
        super().fill(self.color)
        self.kuutio=super().get_size()

class Ipala(pygame.surface.Surface):
    def __init__(self, koko):
        self.color = (0, 191, 255)
        self.rect = pygame.surface.Surface((koko, koko))
        self.muoto = [[0, 4*koko],
                      [0, 3*koko],
                      [0, 2*koko],
                      [0, koko]]
        super().__init__((koko, koko))
        super().fill((self.color))



class Spala(pygame.surface.Surface):
    def __init__(self, koko):
        self.color = (0, 255, 0)
        self.rect = pygame.surface.Surface((koko, koko))
        self.muoto = [[0,koko],
                      [koko, koko],
                      [koko,0],
                      [2*koko,0]]
        super().__init__((koko,koko))
        super().fill((self.color))

class Zpala(pygame.surface.Surface):
    def __init__(self, koko):
        self.color = (255, 0, 0)
        self.rect = pygame.surface.Surface((koko, koko))
        self.muoto = [[koko, 0],
                      [koko, koko],
                      [0, koko],
                      [0,2*koko]]
        super().__init__((koko,koko))
        super().fill((self.color))


class Jpala(pygame.surface.Surface):
    def __init__(self, koko):
        self.color = (0, 0, 139)
        self.rect = pygame.surface.Surface((koko, koko))
        self.muoto = [[0,2*koko],
                      [0,3*koko],
                      [0,koko],
                      [koko, koko]]
        super().__init__((koko,koko))
        super().fill((self.color))


class Npala(pygame.surface.Surface):
    def __init__(self, koko):
        self.color = (255, 255, 0)
        self.rect = pygame.surface.Surface((koko, koko))
        self.muoto = [[koko, koko ],
                      [2*koko,koko],
                      [koko,2*koko],
                      [2*koko,2*koko]]
        super().__init__((koko,koko))
        super().fill((self.color))


class Tpala(pygame.surface.Surface):
    def __init__(self, koko):
        self.color = (255, 0, 255)
        self.rect = pygame.surface.Surface((koko, koko))
        self.muoto = [[koko,0],
                      [2*koko,0],
                      [2*koko,koko],
                      [3*koko,0]]
        super().__init__((koko,koko))
        super().fill((self.color))
