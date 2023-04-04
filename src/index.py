import pygame
from taso import Taso

def main():
    pygame.init()
    pygame.display.set_caption("Tetris")
    ruutu = pygame.display.set_mode((1280,1280))
    tausta = pygame.Surface(ruutu.get_size())
    tausta.fill((0,0,0))
    tausta = tausta.convert()
    taso = Taso(1280,1280)
    #logiiikka ei vielä omassa kansiossaan
    while True:
        ruutu.blit(tausta,(0,0))
        pygame.display.flip()

if __name__ =="__main__":
    main()

