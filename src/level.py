import random
import pygame
from sprites.blocks import Sblock, Jblock, Lblock, Nblock, Iblock, Tblock, Zblock, Block
SIZE =40
class Level(pygame.sprite.OrderedUpdates):

    def __init__(self):
        super().__init__()
        self.x_x,self.y_y=0,0
        self.make_grid()
        self.new_block=None
        self.ended=False
        self.row_cleared=0
        self.block()
        self.is_row_complete()

    def block(self):
        new_block=self.new_block or random_block()
        if Block.hits(new_block,self):
            self.ended= True
        self.add(new_block)
        self.new_block=random_block()
        self.update_grid()
        self.is_row_complete()

    def is_row_complete(self):
        for i in self.grid:
            if i.count(1)>9:
                #jos alin rivi tulee täyteen, niin se tyhjenee mut muuten ei skulaa
                self.row_cleared+=1
                for j in self.sprites():
                    j.y_axel+=1
                for k in range(10):
                    i[k]=0

    def update_grid(self):
        for i in range(20):
            for j in range(10):
                for k in self.sprites():
                    if k.rect.collidepoint(((j*SIZE),(i*SIZE))):
                        self.grid[i][j] = 1
    @property
    def latest(self):
        return self.sprites()[-1]

    def make_grid(self):
        self.grid = [[0 for i in range(10)] for j in range(20)]

    def drop(self):
        self.latest.drop(self)

        if self.latest.current is False:
            self.block()
    def left(self):
        self.latest.left(self)

    def right(self):
        self.latest.right(self)

    def rotate(self):
        self.latest.rotate(self)

    def end_game(self):
        return self.ended

    def score_increase(self):
        return self.row_cleared
def random_block():
    return random.choice((Sblock,Jblock,Lblock,Nblock,Iblock,Zblock,Tblock))()
