
import pygame
import sys
from pygame.locals import *


pygame.init()
clock = pygame.time.Clock()

#nastavenia okna
window = pygame.display.set_mode((800, 500))
BIELA = (255, 255, 255)
CIERNA = (0,0,0)

#horna lista
pygame.display.set_caption("Hangman")
logo = pygame.image.load("001-hangman.png")
pygame.display.set_icon(logo)

#obrazok hangmana
OBRAZKY = []
hangman_status = 0

for i in range(7):
    image = pygame.image.load(f"obrázky/Hangman{i}.png")
    OBRAZKY.append(image)




#tlacidla

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        window.fill(BIELA)
        window.blit(OBRAZKY[hangman_status], (150, 100))
        pygame.display.update()
        clock.tick(50)




