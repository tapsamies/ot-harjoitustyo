# import random
import pygame
from sprites.palat import Spala, Jpala, Lpala, Npala, Ipala, Tpala, Zpala


class Taso(pygame.sprite.Group):
    def __init__(self, koko):
        self.koko = koko
        self.s_p = Spala(koko)
        self.j_p = Jpala(koko)
        self.l_p = Lpala(koko)
        self.n_p = Npala(koko)
        self.p_p = Ipala(koko)
        self.t_p = Tpala(koko)
        self.z_p = Zpala(koko)

    def pala(self, ruutu, x_akseli, y_akseli):
        # self.x_akseli+=1
        y_akseli += 0.05
        for i in self.l_p.muoto:
            ruutu.blit(self.l_p, (i[0]+x_akseli, i[1]+y_akseli))
        # return ruutu.blit(self.l_p,(x_akseli,y_akseli)) or ruutu.blit(self.l_p,(x_akseli,y_akseli))
        # palat=[self.j_p,self.l_p,self.n_p,self.p_p,self.s_p,self.t_p,self.z_p]
        # return pygame.surface.Surface(self.s_p(koko))
        # return  list(palat[random.randint(0,len(palat))])
