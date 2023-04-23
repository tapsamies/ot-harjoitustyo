import random
import pygame
from sprites.palat import Spala, Jpala, Lpala, Npala, Ipala, Tpala, Zpala


class Taso(pygame.sprite.Group):
    def __init__(self, koko):
        self.x,self.y=0,0
        self.koko = koko
        self.s_p = Spala(koko)
        self.j_p = Jpala(koko)
        self.l_p = Lpala(koko)
        self.n_p = Npala(koko)
        self.p_p = Ipala(koko)
        self.t_p = Tpala(koko)
        self.z_p = Zpala(koko)
        self.palikka= self.satunnainen_palikka()

    def piirra(self, ruutu):
        if self.palikka is self.l_p:
            print(self.l_p.kuutio)
        for i in self.palikka.muoto:
            lev=i[0]+self.x
            kork=i[1]+self.y
            ruutu.blit(self.palikka, (lev, kork))
            if kork > 200:
                self.mask = pygame.mask.from_surface(ruutu)
    def pala(self,ruutu,x_akseli):
        self.piirra(ruutu)
        self.x=x_akseli
        self.y+=1
        if self.y <600:
            return True
        else:
            return False
    def nollaa(self):
        self.y=0
        self.x=0
        self.palikka= self.satunnainen_palikka()
    def satunnainen_palikka(self):
        return random.choice((self.l_p,self.p_p,self.s_p,self.j_p,self.z_p,self.n_p,self.t_p))
