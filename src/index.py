import pygame
from taso import Taso 
KOKO = 30
KORKEUS = 30
LEVEYS = 25


def main():
    pygame.init()
    pygame.display.set_caption("Tetris")
    teksti = pygame.font.Font(pygame.font.get_default_font(),18)
     
    korkeus = KORKEUS*KOKO
    leveys = LEVEYS*KOKO
    ruutu = pygame.display.set_mode((leveys, korkeus))
    palaa= pygame.image.load("src/assets/nelio.png")
    x,y=0,0
    sana = teksti.render("AAAA",True,(200,200,0),(100,100,100))
    # logiiikka ei vielä omassa kansiossaan
    while True:
        
        ruutu.fill((110, 110, 110))
        ruutu.blit(palaa, (x, y))
        ruutu.blit(sana,(200,200))
        pygame.draw.line(ruutu,(0,0,0),(0,0),(100,100))
        y+=0.1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        pygame.display.update()

if __name__ == "__main__":
    main()
