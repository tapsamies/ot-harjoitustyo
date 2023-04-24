import pygame
koko=40
class Lpala(pygame.sprite.Sprite):
    def __init__(self):
        self.color = (255, 165, 0)
        self.koko=koko
        self.muoto = [[1,0],
                      [1,0],
                      [1,1]]
        draw(self)


class Ipala(pygame.sprite.Sprite):
    def __init__(self):
        self.color = (0, 191, 255)
        self.koko=koko
        self.muoto = [[1,0],
                      [1,0],
                      [1,0],
                      [1,0]]
        draw(self)


class Spala(pygame.sprite.Sprite):
    def __init__(self):
        self.color = (0, 255, 0)
        self.koko=koko
        self.muoto = [[1,0],
                      [1, 1],
                      [0,1]]
        draw(self)


class Zpala(pygame.sprite.Sprite):
    def __init__(self):
        self.color = (255, 0, 0)
        self.koko=koko
        self.muoto = [[0, 1],
                      [1, 1],
                      [1, 0]]
        draw(self)

class Jpala(pygame.sprite.Sprite):
    def __init__(self):
        self.color = (0, 0, 139)
        self.koko=koko
        self.muoto = [[0,1],
                      [0,1],
                      [1,1]]
        draw(self)

class Npala(pygame.sprite.Sprite):
    def __init__(self):
        self.color = (255, 255, 0)
        self.koko=koko
        self.muoto = [[1,1],
                      [1,1]]
        draw(self)


class Tpala(pygame.sprite.Sprite):
    def __init__(self):
        self.color = (255, 0, 255)
        self.koko=koko
        self.muoto = [[1,0],
                      [1,1],
                      [1,0]]
        draw(self)

def draw(self,x_akseli=4, y_akseli=0):
    self.leveys=len(self.muoto[0])*self.koko
    self.korkeus=len(self.muoto)*self.koko
    self.image = pygame.Surface((self.leveys,self.korkeus))
    self.image.set_colorkey((0,0,0))
    self.rect = pygame.Rect(0,0,self.leveys,self.korkeus)
    for y_akseli, row in enumerate(self.muoto):
        for x_akseli, col in enumerate(row):
            if col:
                pygame.draw.rect(
                        self.image,
                        self.color,
                        pygame.Rect(x_akseli*self.koko+1,y_akseli*self.koko+1,
                                    self.koko-2,self.koko-2))
def tee_muoto(self):
    self.mask= pygame.mask.from_surface(self.image)
