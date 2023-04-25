import pygame
KOKO=40

class Palikka(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.draw()
        self.muoto=list(self.muoto)
        self.mask=None

    def draw(self,x_akseli=4, y_akseli=0):
        self.leveys=len(self.muoto[0])*KOKO
        self.korkeus=len(self.muoto)*KOKO
        self.image = pygame.Surface((self.leveys,self.korkeus))
        self.image.set_colorkey((0,0,0))
        self.rect = pygame.Rect(0,0,self.leveys,self.korkeus)
        self.x_akseli=x_akseli
        self.y_akseli=y_akseli

        for i, row in enumerate(self.muoto):
            for j, col in enumerate(row):
                if col:
                    pygame.draw.rect(
                            self.image,
                            self.color,
                            pygame.Rect(j*KOKO+1,i*KOKO+1,
                                        KOKO-2,KOKO-2))
        self.tee_mask()

    def tee_mask(self):
        #tarvitaan törmäystä varten
        self.mask= pygame.mask.from_surface(self.image)

    def rdraw(self):
        #tähän tulee toiminnallisuus uuden palan piirtämistä varten
        self.draw(self.x_akseli,self.y_akseli)

#Palojen muodot + värit

class Lpala(Palikka):
    color = (255, 165, 0)
    muoto = [[1,0],
             [1,0],
             [1,1]]


class Ipala(Palikka):
    color = (0, 191, 255)
    muoto = [[1,0],
             [1,0],
             [1,0],
             [1,0]]


class Spala(Palikka):
    color = (0, 255, 0)
    muoto = [[1,0],
             [1, 1],
             [0,1]]


class Zpala(Palikka):
    color = (255, 0, 0)
    muoto = [[0, 1],
             [1, 1],
             [1, 0]]

class Jpala(Palikka):
    color = (0, 0, 139)
    muoto = [[0,1],
             [0,1],
             [1,1]]

class Npala(Palikka):
    color = (255, 255, 0)
    muoto = [[1,1],
            [1,1]]


class Tpala(Palikka):
    color = (255, 0, 255)
    muoto = [[1,0],
             [1,1],
             [1,0]]
