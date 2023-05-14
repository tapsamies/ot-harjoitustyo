import pygame
from game_loop import GameLoop

SIZE = 40


def main():

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Tetris")
    game_loop= GameLoop(SIZE, clock)
    game_loop.run()

if __name__ == "__main__":
    main()
