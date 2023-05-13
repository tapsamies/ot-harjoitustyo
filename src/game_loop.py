import pygame
from user_interface import GameScreen
from level import Level
class GameLoop:
    def __init__(self, size, clock):
        self.time=0
        self.level = Level()
        self.clock = clock
        self.size = size
        self._user_interface = GameScreen(self.level)
        self.pause = True
        self.running = True
        self.score = 0
        self.run()


    def run(self):
        while self.running is True:
            if pygame.time.get_ticks()-self.time >1000:
                if self.pause is False:
                    self.level.drop()
                self.time=pygame.time.get_ticks()
            self.actions()
            self.interface()
            #if self.level.line_completed():
             #   self.score+=10
            self.clock.tick(60)

    def actions(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.pause is False:
                    self.level.left()
                if event.key == pygame.K_RIGHT and self.pause is False:
                    self.level.right()
                if event.key == pygame.K_DOWN and self.pause is False:
                    self.level.drop()
                if event.key == pygame.K_UP and self.pause is False:
                    self.level.rotate()
                if event.key == pygame.K_SPACE:
                    self.pause = not self.pause
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x,m_y=pygame.mouse.get_pos()
                if m_x in range(self.size*12,self.size*13) and m_y<self.size:
                    self.pause = not self.pause
            elif event.type == pygame.QUIT:
                self.running=False

    def interface(self):
        if self.pause is False:
            self._user_interface.show()
        if self.pause is True:
            self._user_interface.pause()
