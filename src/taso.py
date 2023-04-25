import random
import pygame
from sprites.palat import Spala, Jpala, Lpala, Npala, Ipala, Tpala, Zpala
KOKO = 40

class Taso(pygame.sprite.OrderedUpdates):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.x_x,self.y_y=0,0
        self.koko = KOKO
        self.palikka= satunnainen_palikka()
        self.uus_pala=None
        self.palikat=[]

    def piirra(self, ruutu):
        #pala piirtyy kuvana johonkin päin ruutua,
        #mutta ei pysty vielä muuten tekemään ruudukossa mitään
        ruutu.blit(self.palikka.image, (self.x_x,self.y_y))

    def pala(self,ruutu,x_akseli):

        uusi_palikka=self.uus_pala or satunnainen_palikka()
        self.uus_pala=satunnainen_palikka()
        self.add(uusi_palikka)
        #yläpuolella olevat 3 riviä vielä tee mitään näkyvää
        self.x_x=x_akseli
        self.piirra(ruutu)

    def nollaa(self):
        self.y_y=0
        self.palikka= satunnainen_palikka()

    def tipu(self):
        self.y_y+=3


def satunnainen_palikka():
    return random.choice((Spala,Jpala,Lpala,Lpala,Npala,Ipala,Zpala,Tpala))()
