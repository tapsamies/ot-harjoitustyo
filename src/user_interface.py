import pygame
SIZE = 40

class GameScreen:
    def __init__(self, level):
        self.display = pygame.display.set_mode((SIZE*14,SIZE*20))
        self.level = level
        self.height = self.display.get_height()
        self.width = self.display.get_width()
        self.font = pygame.font.Font(pygame.font.get_default_font(),18)
        self.color = (0,0,0)
        self.h_light= (255,255,255)

    def show(self,score):
        self.level.draw(self.display)
        self.display.fill((0,0,0))

        for i in range(0,11):
            pygame.draw.lines(self.display,(110, 110, 110),True,
                              ((i*SIZE, 0), (i*SIZE, SIZE*20)))

        for i in range(0, 21):
            pygame.draw.lines(self.display, (110, 110, 110), True,
                              ((0, i*SIZE), (SIZE*10, i*SIZE)))
        self.level.draw(self.display)
        self.writer(f"Score: {score}",(self.width*0.85,50))
        self.settings_icon()
        self.pause_icon()
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

    def end_screen(self,score):
        self.level.draw(self.display)
        self.display.fill((0,0,0))
        self.writer("Game Over, press R to restart",(200,200))
        self.writer(f"Your score was:{score}",(300,300))
        pygame.display.update()

    def writer(self,string,position):
        self.display.blit(self.font.render(f"{string}",True,self.color,self.h_light),(position))

    def settings_icon(self):
        #Tämä kaunis viritelmä ottaa ikkunan koon huomioon ikonia piirtäessä
        #Ikonilla ei voi tehdä mitään
        settings_icon= [[self.width-SIZE*0.675,0],
                        [self.width-SIZE*0.75,SIZE*0.075],
                        [self.width-SIZE*0.625,SIZE*0.225],
                        [self.width-SIZE*0.7,SIZE*0.325],
                        [self.width-SIZE*0.9,SIZE*0.175],
                        [self.width-SIZE,SIZE*0.275],
                        [self.width-SIZE*0.775,SIZE*0.5],
                        [self.width-SIZE*0.625,SIZE*0.425],
                        [self.width-SIZE*0.075,SIZE],
                        [self.width-0,SIZE*0.875],
                        [self.width-SIZE*0.525,SIZE*0.35],
                        [self.width-SIZE*0.425,SIZE*0.175]]
        pygame.draw.polygon(self.display,self.h_light,settings_icon)
    def pause_icon(self):
        pygame.draw.line(self.display,self.h_light,(self.width-80,0),(self.width-80,20),4)
        pygame.draw.line(self.display,self.h_light,(self.width-72,0),(self.width-72,20),4)
