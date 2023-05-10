import pygame




class GameScreen:
    def __init__(self, display,level):
        self.display = display
        self.level = level
        self.height = self.display.get_height()
        self.width = self.display.get_width()
        self.size = self.height//20
        self.font = pygame.font.Font(pygame.font.get_default_font(),18)
        self.word = self.font.render("Press ESC to resume",True,(69,69,69),(255,255,255))
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
    def pause(self):
        self.level.draw(self.display)
        self.display.fill((100,100,100))
        self.display.blit(self.word,(200,200))
        pygame.display.update()
