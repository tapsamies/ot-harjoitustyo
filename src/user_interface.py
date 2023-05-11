import pygame




class GameScreen:
    def __init__(self, display,level):
        self.display = display
        self.level = level
        self.height = self.display.get_height()
        self.width = self.display.get_width()
        self.size = self.height//20
        self.font = pygame.font.Font(pygame.font.get_default_font(),18)
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
        pygame.draw.rect(self.display,(0,0,0),(self.display.get_width()*0.1,
                                               self.display.get_height()*0.1,
                                               self.display.get_width()*0.8,
                                               self.display.get_height()*0.8))
        self.display.blit(self.font.render("Press ESC to start",True,(69,69,69),(255,255,255)),(200,200))
        self.display.blit(self.font.render("Press R to restart",True,(69,69,69),(255,255,255)),(200,250))
        pygame.display.update()
