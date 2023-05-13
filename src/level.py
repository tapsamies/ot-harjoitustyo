import random
import pygame
from sprites.blocks import Sblock, Jblock, Lblock, Nblock, Iblock, Tblock, Zblock, Block
SIZE =40
class Level(pygame.sprite.OrderedUpdates):

    def __init__(self):
        super().__init__()
        self.x_x,self.y_y=0,0
        self.size=SIZE
        self.make_grid()
        self.new_block=None
        self.block()
        self.is_row_complete()

    def block(self):
        new_block=self.new_block or random_block()
        #if Block.hits(new_block,self):
         #   pygame.quit()
        self.add(new_block)
        self.new_block=random_block()

    def is_row_complete(self):
        pass


    @property
    def latest(self):
        print(self.sprites())
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

def random_block():
    return random.choice((Sblock,Jblock,Lblock,Nblock,Iblock,Zblock,Tblock))()
