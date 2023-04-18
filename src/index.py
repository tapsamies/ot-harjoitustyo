import pygame
from taso import Taso
from tapahtumat import Nappain
KOKO = 40
KORKEUS = 20
LEVEYS = 14


def main():
    pygame.init()
    kello = pygame.time.Clock()
    pygame.display.set_caption("Tetris")
    teksti = pygame.font.Font(pygame.font.get_default_font(), 18)
    oikea, vasen = False, False
    korkeus = KORKEUS*KOKO
    leveys = LEVEYS*KOKO
    ruutu = pygame.display.set_mode((leveys, korkeus))
    # palaa= pygame.image.load("src/assets/nelio.png")
    palaa = pygame.surface.Surface((KOKO, KOKO))
    pala = Taso(KOKO)
    palaa.fill((255, 255, 255))
    pisteet = 0
    x_akseli, y_akseli = 0, 0
    # palaa.get_width()
    sana = teksti.render(f"Pisteet: {pisteet}",
                         True, (200, 200, 0), (100, 100, 100))
    # logiiikka ei vielä omassa kansiossaan
    while True:
        ruutu.fill((0, 0, 0))
        ruutu.blit(sana, (leveys-sana.get_width(), 0))
        for i in range(0, 11):
            pygame.draw.lines(ruutu, (110, 110, 110), True,
                              ((i*KOKO, 0), (i*KOKO, korkeus)))
        for i in range(0, 21):
            pygame.draw.lines(ruutu, (110, 110, 110), True,
                              ((0, i*KOKO), (KOKO*10, i*KOKO)))
        # ruutu.blit(palaa, (x_akseli, y_akseli))
        # ruutu.blit(pala.p_p , (x_akseli, y_akseli))
        pala.pala(ruutu, x_akseli, y_akseli)
        if y_akseli < korkeus-pala.p_p.get_height():
            y_akseli += 1
        for event in Nappain.get(main):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    vasen = True
                if event.key == pygame.K_RIGHT:
                    oikea = True
                if event.key == pygame.K_DOWN:
                    y_akseli = korkeus-palaa.get_height()-1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    vasen = False
                if event.key == pygame.K_RIGHT:
                    oikea = False
            if event.type == pygame.QUIT:
                return False
        if vasen and x_akseli >= 0:
            x_akseli -= 5
        if oikea and x_akseli <= 9*KOKO-KOKO*3:  # palikan koko pitäs selvittää
            x_akseli += 5
        kello.tick(60)
        pygame.display.update()


if __name__ == "__main__":
    main()
