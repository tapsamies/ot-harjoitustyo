import random
import pygame
from sprites.palat import Spala, Jpala, Lpala, Npala, Ipala, Tpala, Zpala
koko = 40

class Taso(pygame.sprite.OrderedUpdates):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.x,self.y=0,0
        self.koko = koko
        self.palikka= self.satunnainen_palikka()
        self.uus_pala=None

    def piirra(self, ruutu):
        lev=self.x
        kork=self.y
        return ruutu.blit(self.palikka.image, (lev, kork))
    def pala(self,ruutu,x_akseli):
        self.uus_pala=self.piirra(ruutu)
        self.x=x_akseli
        self.y+=2
        self.add(self.uus_pala)
        #uusi_pala.y+=2
        if self.y <self.koko*20:
            return True
        else:
            self.nollaa()
    def nollaa(self):
        self.y=0
        #self.x=0
        self.palikka= self.satunnainen_palikka()
    def satunnainen_palikka(self):
        return random.choice((Spala,Jpala,Lpala,Lpala,Npala,Ipala,Zpala))()
        #return random.choice((self.l_p,self.p_p,self.s_p,self.j_p,self.z_p,self.n_p,self.t_p))
    def osuu(self):
        self.korkeus=self.koko
        self.leveys=self.koko
        self.pelialue=pygame.Rect((0,0,self.leveys,self.korkeus))
        return self.palikka.rect.colliderect(self.pelialue)
