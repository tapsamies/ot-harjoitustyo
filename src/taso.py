import random
import pygame
from sprites.palat import Spala, Jpala, Lpala, Npala, Ipala, Tpala, Zpala
KOKO = 40

class Taso(pygame.sprite.Group):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.x_x,self.y_y=0,0
        self.ruudukko=None
        self.uus_pala=None
        self.piirra()
        self.pala()

    def piirra(self):
        pass

    def teetee(self):
        pass

    def pala(self):

        uusi_palikka=self.uus_pala or satunnainen_palikka()
        self.add(uusi_palikka)
        self.uus_pala=satunnainen_palikka()
        self.piirra()
        self.teetee()

    @property
    def spritet(self):
        return [i for i in self.sprites()[:-1]]

    @property
    def uusin(self):
        return self.sprites()[-1]
    @property
    def osuu(self):
        pass
        #for i in self.spritet:
         #   if pygame.sprite.collide_mask(self.uusin,i) is not None:
          #      return True
        #    return pygame.sprite.collide_rect(self.uusin,i)
        #return pygame.sprite.spritecollideany(self.uusin,self.spritet)


    def tiputa(self):

        if self.uusin.nykyinen is False or self.osuu is True:
            #self.uusin.nykyinen=True
            self.pala()
        else:
            self.uusin.tipu(self)
    def vasen(self):
        if self.osuu is False:
            self.uusin.vasempaan(self)

    def oikea(self):
        if self.osuu is False:
            self.uusin.oikeaan(self)

def satunnainen_palikka():
    return random.choice((Spala,Jpala,Lpala,Lpala,Npala,Ipala,Zpala,Tpala))()
