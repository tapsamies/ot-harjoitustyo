import pygame




class GameScreen:
    def __init__(self, display,level):
        self.display = display
        self.level = level
        self.height = self.display.get_height()
        self.width = self.display.get_width()
        self.size = self.height//20

    def show(self):
        self.level.draw(self.display)
        self.display.fill((0,0,0))

        for i in range(0,11):
            pygame.draw.lines(self.display,(110, 110, 110),True,
                              ((i*self.size, 0), (i*self.size, self.height)))


        for i in range(0, 21):
            pygame.draw.lines(self.display, (110, 110, 110), True,
                              ((0, i*self.size), (self.size*10, i*self.size)))
        self.level.draw(self.display)
        pygame.display.update()
