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
    def uusin(self):
        return self.sprites()[-1]

    def tiputa(self):
        self.uusin.tipu(self)

        if self.uusin.nykyinen is False:
            #self.uusin.nykyinen=True
            self.pala()
    def vasen(self):
        self.uusin.vasempaan(self)

    def oikea(self):
        self.uusin.oikeaan(self)

def satunnainen_palikka():
    return random.choice((Spala,Jpala,Lpala,Npala,Ipala,Zpala,Tpala))()
