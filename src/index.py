import pygame
from level import Level
from user_interface import GameScreen
from game_loop import GameLoop

SIZE = 40
HEIGHT = 20*SIZE
WIDTH = 14*SIZE


def main():

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Tetris")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    level = Level()
    user_interface= GameScreen(screen,level)
    game_loop= GameLoop(level,SIZE,clock,user_interface)
    game_loop.run()

if __name__ == "__main__":
    main()
