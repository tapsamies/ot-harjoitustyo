import pygame
SIZE=40

class Block(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.shape=list(self.shape)
        self.mask=None
        self.current=True
        self.size=SIZE
        self.draw()

    def draw(self,x_axel=4, y_axel=-2):
        self.width=len(self.shape[0])*self.size
        self.height=len(self.shape)*self.size
        self.image = pygame.Surface((self.width,self.height))
        self.image.set_colorkey((0,0,0))
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.x_axel=x_axel
        self.y_axel=y_axel

        for i, row in enumerate(self.shape):
            for j, col in enumerate(row):
                if col:
                    pygame.draw.rect(
                            self.image,
                            self.color,
                            pygame.Rect(j*self.size+1,i*self.size+1,
                                        self.size-2,self.size-2))
        self.do_mask()

    def do_mask(self):
        self.mask= pygame.mask.from_surface(self.image)

    def hits(self,group):
        for i in group:
            if i == self:
                continue
            if pygame.sprite.collide_mask(self,i) is not None:
                return True
        return False


    @property
    def group(self):
        return self.groups()
    @property
    def nyt(self):
        return self.sprites()[-1]

    @property
    def y_axel(self):
        return self._y_axel

    @y_axel.setter
    def y_axel(self, value):
        self._y_axel = value
        self.rect.top = value*self.size

    @property
    def x_axel(self):
        return self._x_axel

    @x_axel.setter
    def x_axel(self,value):
        self._x_axel = value
        self.rect.left = value*self.size

    def drop(self,group):
        self.y_axel+=1
        if self.rect.bottom > self.size*20 or self.hits(group) is True:
            self.y_axel-=1
            self.current= False

    def right(self,group):
        self.x_axel+=1
        if self.rect.right > self.size*10 or self.hits(group) is True:
            self.x_axel-=1

    def left(self,group):
        self.x_axel-=1
        if self.x_axel < 0 or self.hits(group) is True:
            self.x_axel +=1

    def rotate(self,group):
        rows = len(self.shape)
        cols = len(self.shape[0])
        rotated = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                rotated[j][rows - 1 -i] = self.shape[i][j]
        if self.hits(group) is False:
            self.shape = rotated


        for i in self.shape:
            if self.rect.right > self.size*10 or self.hits(group) is True:
                self.x_axel-=1
            if self.x_axel < 0 or self.hits(group) is True:
                self.x_axel +=1
            if self.hits(group) is True or self.rect.bottom > self.size*20:
                self.y_axel-=1

            self.draw(self._x_axel,self._y_axel)

#Palojen muodot + värit

class Lblock(Block):
    color = (255, 165, 0)
    shape = [[1,0],
             [1,0],
             [1,1]]


class Iblock(Block):
    color = (0, 191, 255)
    shape = [[1],
             [1],
             [1],
             [1]]


class Sblock(Block):
    color = (0, 255, 0)
    shape = [[1,0],
             [1, 1],
             [0,1]]


class Zblock(Block):
    color = (255, 0, 0)
    shape = [[0, 1],
             [1, 1],
             [1, 0]]

class Jblock(Block):
    color = (0, 0, 139)
    shape = [[0,1],
             [0,1],
             [1,1]]

class Nblock(Block):
    color = (255, 255, 0)
    shape = [[1,1],
            [1,1]]


class Tblock(Block):
    color = (255, 0, 255)
    shape = [[1,1,1],
             [0,1,0]]
