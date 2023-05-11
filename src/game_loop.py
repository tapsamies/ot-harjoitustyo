import pygame



class GameLoop:
    def __init__(self, level, size, clock, user_interface):
        self.level = level
        self.size = size
        self.clock = clock
        self._user_interface = user_interface
        self.pause = True
        self.running = True
        self.score = 0
        self.run()


    def run(self):
        while self.running is True:
            self.actions()
            self.interface()
            #if self.level.line_completed():
             #   self.score+=10
            self.clock.tick(60)
            self.clock.get_time()

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
                if event.key == pygame.K_ESCAPE:
                    self.pause = not self.pause
            elif event.type == pygame.QUIT:
                self.running=False

    def interface(self):
        if self.pause is False:
            self._user_interface.show()
        if self.pause is True:
            self._user_interface.pause()
