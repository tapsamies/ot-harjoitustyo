import pygame

class l_pala(pygame.surface.Surface):
    def __init(self,KOKO):
        super().__init__()
        self.color = (255,165,0)
        self.rect = pygame.surface.Surface((KOKO,KOKO))
        self.muoto= [[1,0],
                     [1,0],
                     [1,1]]

class i_pala(pygame.surface.Surface):
    def __init(self,KOKO):
        super().__init__()
        self.color =(0,191,255)
        self.rect = pygame.surface.Surface((KOKO,KOKO))
        self.muoto= [[1],[1],[1],[1]]

class s_pala(pygame.surface.Surface):
    def __init(self,KOKO):
        super().__init__()
        self.color = (0,255,0)
        self.rect = pygame.surface.Surface((KOKO,KOKO))
        self.muoto= [[0,1,1],
                     [1,1,0]]

class z_pala(pygame.surface.Surface):
    def __init(self,KOKO):
        super().__init__()
        self.color = (255,0,0)
        self.rect = pygame.surface.Surface((KOKO,KOKO))
        self.muoto= [[1,1,0],[0,1,1]]

class j_pala(pygame.surface.Surface):
    def __init(self,KOKO):
        super().__init__()
        self.color = (0,0,139)
        self.rect = pygame.surface.Surface((KOKO,KOKO))
        self.muoto= [[0,1],
                     [0,1],
                     [1,1]]

class n_pala(pygame.surface.Surface):
    def __init(self,KOKO):
        super().__init__()
        self.color = (255,255,0)
        self.rect = pygame.surface.Surface((KOKO,KOKO))
        self.muoto= [[2,2],
                     [2,2]]

class t_pala(pygame.surface.Surface):
    def __init(self,KOKO):
        super().__init__()
        self.color = (255,0,255)
        self.rect = pygame.surface.Surface((KOKO,KOKO))
        self.muoto= [[1,1,1],
                     [0,1,0]]
                     
