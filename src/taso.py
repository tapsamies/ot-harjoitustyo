import pygame
from sprites.j_pala import j_pala
from sprites.l_pala import l_pala
from sprites.nelio import nelio
from sprites.pitkula import pitkula
from sprites.s_pala import s_pala
from sprites.t_pala import t_pala
from sprites.z_pala import z_pala




class Taso:
    def __init__(self,korkeus,leveys):
        """
        ideana on se että peliruudukko vie ~85% näytöllä olevasta tilasta
        loput tilasta tulee pistelaskurille, seuraaville paloille ja 
        yksinkertaiselle valikolle.
        """
        self.solu_x=0.9*leveys/10
        self.solu_y=0.95*korkeus/20
        s_pala().muoto
