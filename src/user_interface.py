import pygame
SIZE = 40

class GameScreen:
    def __init__(self, level):
        self.size = SIZE
        self.display = pygame.display.set_mode((self.size*14,self.size*20))
        self.level = level
        self.height = self.display.get_height()
        self.width = self.display.get_width()
        self.font = pygame.font.Font(pygame.font.get_default_font(),18)
        self.color = (0,0,0)
        self.h_light= (255,255,255)

    def show(self):
        self.level.draw(self.display)
        self.display.fill((0,0,0))

        for i in range(0,11):
            pygame.draw.lines(self.display,(110, 110, 110),True,
                              ((i*self.size, 0), (i*self.size, self.size*20)))

        for i in range(0, 21):
            pygame.draw.lines(self.display, (110, 110, 110), True,
                              ((0, i*self.size), (self.size*10, i*self.size)))
        self.level.draw(self.display)
        self.writer("Score",(self.width*0.9,50))
        self.icons()
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

    def icons(self):
        #Tämä kaunis viritelmä mahdollistaa ikonin skaalautumisen
        settings_icon= [[self.width-self.size*0.675,0],
                        [self.width-self.size*0.75,self.size*0.075],
                        [self.width-self.size*0.625,self.size*0.225],
                        [self.width-self.size*0.7,self.size*0.325],
                        [self.width-self.size*0.9,self.size*0.175],
                        [self.width-self.size,self.size*0.275],
                        [self.width-self.size*0.775,self.size*0.5],
                        [self.width-self.size*0.625,self.size*0.425],
                        [self.width-self.size*0.075,self.size],
                        [self.width-0,self.size*0.875],
                        [self.width-self.size*0.525,self.size*0.35],
                        [self.width-self.size*0.425,self.size*0.175]]
        pygame.draw.polygon(self.display,self.h_light,settings_icon)

        pygame.draw.line(self.display,self.h_light,(self.width-80,0),(self.width-80,20),4)
        pygame.draw.line(self.display,self.h_light,(self.width-72,0),(self.width-72,20),4)
