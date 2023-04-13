import pygame
import random
from sprites.j_pala import j_pala
from sprites.l_pala import l_pala
from sprites.nelio import nelio
from sprites.pitkula import pitkula
from sprites.s_pala import s_pala
from sprites.t_pala import t_pala
from sprites.z_pala import z_pala


class Taso:
    def __init__(self, korkeus, leveys):
        self.s=s_pala(korkeus, leveys)
        self.j=j_pala(korkeus,leveys)
        self.l=l_pala(korkeus,leveys)
        self.n=nelio(korkeus,leveys)
        self.p=pitkula(korkeus,leveys)
        self.t=t_pala(korkeus,leveys)
        self.z=z_pala(korkeus,leveys)
    def pala(self):
        return random.choice([self.j,self.l,self.n,self.p,self.s,self.t,self.z])
