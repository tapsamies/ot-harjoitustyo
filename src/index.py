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
    text = pygame.font.Font(pygame.font.get_default_font(), 18)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    score = 0
 #   block= Level()
    word = text.render(f"Pisteet: {score}",
                         True, (200, 200, 0), (100, 100, 100))
    level = Level()
    user_interface= GameScreen(screen,level)
    game_loop= GameLoop(level,SIZE,clock,user_interface)
    game_loop.run()

if __name__ == "__main__":
    main()
