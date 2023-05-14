import pygame
from user_interface import GameScreen
from level import Level
class GameLoop:
    def __init__(self, size, clock):
        self.time=0
        self.level = Level()
        self.clock = clock
        self.size = size
        self.pause = True
        self.running = True
        self.score = 0
        self._user_interface = GameScreen(self.level)
        self.run()


    def run(self):
        while self.running is True:
            if pygame.time.get_ticks()-self.time >1000:
                if self.pause is False:
                    self.level.drop()
                self.time=pygame.time.get_ticks()
            self.actions()
            self.interface()
            self.clock.tick(60)
            self.score=self.level.score_increase()

    def actions(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #ei oo fresh et palat liikkuu pausen aikana
                if event.key == pygame.K_LEFT and self.pause is False:
                    self.level.left()
                if event.key == pygame.K_RIGHT and self.pause is False:
                    self.level.right()
                if event.key == pygame.K_DOWN and self.pause is False:
                    self.level.drop()
                if event.key == pygame.K_UP and self.pause is False:
                    self.level.rotate()
                if event.key == pygame.K_r:
                    self.level=Level()
                    self._user_interface=GameScreen(self.level)
                if event.key == pygame.K_SPACE:
                    self.pause = not self.pause
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.QUIT:
                self.running=False

    def interface(self):
        if self.level.end_game() is True:
            self._user_interface.end_screen(self.score)
#elif -lauseketta käyttämällä ruutu ei ala vilkkumaan eri näyttövaihtoehtojen välillä
        elif self.pause is False:
            self._user_interface.show(self.score)
        elif self.pause is True:
            self._user_interface.pause()
