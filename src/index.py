import pygame
from taso import Taso


KOKO=30
KORKEUS=20
LEVEYS=10

def main():
    pygame.display.set_caption("Tetris")
    korkeus=KORKEUS*KOKO
    leveys=LEVEYS*KOKO
    ruutu = pygame.display.set_mode((korkeus,leveys))
    tausta = pygame.Surface(ruutu.get_size())
    tausta.fill((0,0,0))
    tausta = tausta.convert()
    ataso = Taso(korkeus,leveys)
    #logiiikka ei vielä omassa kansiossaan
    while True:
        ruutu.blit(tausta,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
         


if __name__ =="__main__":
    main()

