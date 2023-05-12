import pygame




class GameScreen:
    def __init__(self, display,level):
        self.display = display
        self.level = level
        self.height = self.display.get_height()
        self.width = self.display.get_width()
        self.size = self.height//20
        self.font = pygame.font.Font(pygame.font.get_default_font(),18)
        self.color = (0,0,0)
        self.h_light= (255,255,255)
        self.settings_icon= [[self.width-27,0],[self.width-30,3],[self.width-25,9],
                             [self.width-28,13],[self.width-36,7],[self.width-40,11],
                             [self.width-31,20],[self.width-25,17],[self.width-3,40],
                             [self.width-0,35],[self.width-21,14],[self.width-17,7]]
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
        self.writer("Score",(self.width*0.9,50))
        pygame.draw.polygon(self.display,self.h_light,self.settings_icon)
        pygame.display.update()
    def pause(self):
        self.level.draw(self.display)
        self.display.fill((100,100,100))
        pygame.draw.rect(self.display,(0,0,0),(self.display.get_width()*0.1,
                                               self.display.get_height()*0.1,
                                               self.display.get_width()*0.8,
                                               self.display.get_height()*0.8))
        self.writer("Press SPACE to start and pause",(200,200))
        self.writer("Press R to restart",(200,250))
        self.writer("Press Esc to Escape",(200,300))

        pygame.display.update()

    def writer(self,string,position):
        self.display.blit(self.font.render(f"{string}",True,self.color,self.h_light),(position))
