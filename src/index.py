import pygame
from taso import Taso 
KOKO = 40
KORKEUS = 20
LEVEYS = 14


def main():
    pygame.init()
    pygame.display.set_caption("Tetris")
    teksti = pygame.font.Font(pygame.font.get_default_font(),18)
    oikea,vasen=False,False 
    korkeus = KORKEUS*KOKO
    leveys = LEVEYS*KOKO

    ruutu = pygame.display.set_mode((leveys, korkeus))
    #palaa= pygame.image.load("src/assets/nelio.png")
    palaa = pygame.surface.Surface((KOKO,KOKO))
    palaa.fill((255,255,255))
    pisteet=0
    x,y=0,0
    nelio_koko=KOKO#palaa.get_width()
    sana = teksti.render(f"Pisteet: {pisteet}",True,(200,200,0),(100,100,100))
    # logiiikka ei vielä omassa kansiossaan
    while True:
        
        ruutu.fill((0, 0, 0))
        ruutu.blit(sana,(leveys-sana.get_width(),0))
        for i in range(0,11):
            pygame.draw.lines(ruutu,(110,110,110),True,((i*nelio_koko,0),(i*nelio_koko,korkeus)))
        for i in range(0,21):
            pygame.draw.lines(ruutu,(110,110,110),True,((0,i*nelio_koko),(nelio_koko*10,i*nelio_koko)))
        ruutu.blit(palaa, (x, y))

        if y <korkeus-palaa.get_height():  
            y+=0.04
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:  
                        vasen=True
                    if event.key == pygame.K_RIGHT:
                        oikea=True
                    if event.key == pygame.K_DOWN:
                        y=korkeus-palaa.get_height()-1
            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        vasen=False
                    if event.key == pygame.K_RIGHT:
                        oikea=False
            if event.type == pygame.QUIT:
                return False
        
        if vasen and x>=0:
            x-=1
        if oikea and x<=9*KOKO:
            x+=1

        
        pygame.display.update()

if __name__ == "__main__":
    main()
