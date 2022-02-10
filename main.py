import pygame
import sys
from pygame.locals import *


pygame.init()
clock = pygame.time.Clock()

#nastavenia okna
window = pygame.display.set_mode((800, 500))
BIELA = (255, 255, 255)
CIERNA = (0,0,0)

#nastavenie hornej listy
pygame.display.set_caption("Hangman")
logo = pygame.image.load("001-hangman.png")
pygame.display.set_icon(logo)

#obrazky hangmana
OBRAZKY = []
stav_hangmana = 0

for i in range(7):
    image = pygame.image.load(f"obrázky/Hangman{i}.png")
    OBRAZKY.append(image)
#tlacidla a vypis pismen do tlacidiel
RIADKY = 2
STLPCE = 13
MEDZERY = 20
VELKOST = 40
OKNA = []


for riadok in range(RIADKY):
    for stlpec in range(STLPCE):
        x = ((stlpec * MEDZERY) + MEDZERY) + (VELKOST * stlpec)
        y = ((riadok * MEDZERY) + MEDZERY) + (VELKOST * riadok) + 350
        okno = pygame.Rect(x,y,VELKOST,VELKOST)
        OKNA.append(okno)
TLACIDLA = []
A = 65
for znak,okno in enumerate(OKNA):
    pismena = chr(A+znak)
    tlacidlo =[okno, pismena]
    TLACIDLA.append(tlacidlo)

#fonty pisma
tlacidlo_font = pygame.font.SysFont("arial", 30)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        window.fill(BIELA)
        window.blit(OBRAZKY[stav_hangmana], (150, 100))
        #vykreslenie tlacidiel
        for okno, pismena in TLACIDLA:
            tlacidlo_text = tlacidlo_font.render(pismena, True, CIERNA)
            tlacidlo_tvar = tlacidlo_text.get_rect(center = (okno.x + 20, okno.y +20))
            window.blit(tlacidlo_text, tlacidlo_tvar)
            pygame.draw.rect(window, CIERNA, okno, 2)


        pygame.display.update()
        clock.tick(50)




