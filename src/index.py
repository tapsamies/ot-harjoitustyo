import pygame
from taso import Taso

SIZE = 40
HEIGHT = 20*SIZE
WIDTH = 14*SIZE


def main():

    pygame.init()
    kello = pygame.time.Clock()
    pygame.display.set_caption("Tetris")
    teksti = pygame.font.Font(pygame.font.get_default_font(), 18)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    score = 0
    block= Taso()
    sana = teksti.render(f"Pisteet: {score}",
                         True, (200, 200, 0), (100, 100, 100))


    while True:

        screen.fill((0, 0, 0))
        screen.blit(sana, (WIDTH-sana.get_width(), 0))


        for i in range(0, 11):
            pygame.draw.lines(screen, (110, 110, 110), True,
                              ((i*SIZE, 0), (i*SIZE, HEIGHT)))
        for i in range(0, 21):
            pygame.draw.lines(screen, (110, 110, 110), True,
                              ((0, i*SIZE), (SIZE*10, i*SIZE)))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    block.vasen()
                if event.key == pygame.K_RIGHT:
                    block.oikea()
                if event.key == pygame.K_DOWN:
                    block.tiputa()

            if event.type == pygame.QUIT:
                return False


        block.draw(screen)
        kello.tick(60)
        pygame.display.update()

if __name__ == "__main__":
    main()
