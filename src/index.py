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
    pala = Taso()
    pisteet = 0
    x_akseli, y_akseli = 0,0
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
        
        if y_akseli < korkeus:
            y_akseli += 1
        else:
            y_akseli=0
        for event in Nappain.get(main):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    vasen = True
                if event.key == pygame.K_RIGHT:
                    oikea = True
                if event.key == pygame.K_DOWN:
                    y_akseli = korkeus
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    vasen = False
                if event.key == pygame.K_RIGHT:
                    oikea = False
                if event.key == pygame.K_UP:
                    kaanna = False
            if event.type == pygame.QUIT:
                return False
        if vasen and x_akseli>=0:
            x_akseli -= KOKO
        if oikea and x_akseli<KOKO*10 :  # palikan koko pitäs selvittää
            x_akseli += KOKO
        kello.tick(60)
        pala.pala(ruutu,x_akseli)
        pygame.display.update()

if __name__ == "__main__":
    main()
