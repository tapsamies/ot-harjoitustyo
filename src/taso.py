import pygame
import random
from sprites.palat import s_pala,j_pala,l_pala,n_pala,i_pala,t_pala,z_pala


class Taso:
    def __init__(self, KOKO):
        self.s=s_pala(KOKO)
        self.j=j_pala(KOKO)
        self.l=l_pala(KOKO)
        self.n=n_pala(KOKO)
        self.p=i_pala(KOKO)
        self.t=t_pala(KOKO)
        self.z=z_pala(KOKO)
    def pala(self):
        return random.choice([self.j,self.l,self.n,self.p,self.s,self.t,self.z])
