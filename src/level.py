import random
import pygame
from sprites.blocks import Sblock, Jblock, Lblock, Nblock, Iblock, Tblock, Zblock
SIZE = 40

class Level(pygame.sprite.Group):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.x_x,self.y_y=0,0
        self.grid=None
        self.new_block=None
        self.block()

    def block(self):

        uusi_palikka=self.new_block or random_block()
        self.add(uusi_palikka)
        self.new_block=random_block()
        #self.teetee()


    @property
    def latest(self):
        return self.sprites()[-1]

    def drop(self):
        self.latest.drop(self)

        if self.latest.current is False:
            #self.latest.current=True
            self.block()
    def left(self):
        self.latest.left(self)

    def right(self):
        self.latest.right(self)

    def rotate(self):
        self.latest.rotate(self)

def random_block():
    return random.choice((Sblock,Jblock,Lblock,Nblock,Iblock,Zblock,Tblock))()
