import button as button
import pygame
import sys
from pygame.locals import *

#vykreslenie tlacidiel
def vykreslenie_tlacidiel(TLACIDLA):
    for okno, pismena in TLACIDLA:
        tlacidlo_text = tlacidlo_font.render(pismena, True, CIERNA)
        tlacidlo_vypisanie = tlacidlo_text.get_rect(center=(okno.x + 20, okno.y + 20))
        window.blit(tlacidlo_text, tlacidlo_vypisanie)
        pygame.draw.rect(window, CIERNA, okno, 2)
def uhadnute_slovo():
    display_text = ""
    for pismena in SLOVO:
        if pismena in UHADNUTE_SLOVO:
            display_text += f"{pismena}"
        else:
            display_text += "_ "
    text = pismeno_font.render(display_text, True, CIERNA)
    window.blit(text, (400, 200))

pygame.init()
clock = pygame.time.Clock()

#nastavenia okna
SIRKA = 800
VYSKA = 500
window = pygame.display.set_mode((SIRKA, VYSKA))
BIELA = (255, 255, 255)
CIERNA = (0,0,0)
#stav hry

koniec_hry = False



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
hra_font = pygame.font.SysFont("arial", 80)
pismeno_font = pygame.font.SysFont("arial", 60)

#zoznam slov
SLOVO = "PYGAME"
UHADNUTE_SLOVO = []


#nadpis pre hru
nadpis = "Hangman"
nadpis_text = hra_font.render(nadpis, True, CIERNA)
nadpis_vypis = nadpis_text.get_rect(center=(SIRKA//2//2+400, hra_font.get_height()//2-10))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            kliknuta_pozicia = event.pos
            for tlacidlo, pismena in TLACIDLA:
                if tlacidlo.collidepoint(kliknuta_pozicia):
                    if pismena not in SLOVO:
                        stav_hangmana +=1
                    if stav_hangmana ==6:
                        koniec_hry = True

                    UHADNUTE_SLOVO.append(pismena)
                    TLACIDLA.remove([tlacidlo, pismena])

    window.fill(BIELA)
    window.blit(OBRAZKY[stav_hangmana], (150, 100))
    window.blit(nadpis_text,nadpis_vypis)
    vykreslenie_tlacidiel(TLACIDLA)
    uhadnute_slovo()
    vyhra = True
    for pismena in SLOVO:
        if pismena not in UHADNUTE_SLOVO:
            vyhra = False
    if vyhra:
        koniec_hry = True
        koniec_hry_vypis = "Vyhral si :)"
    else:
        koniec_hry_vypis = "Prehral si :("




    pygame.display.update()
    clock.tick(50)

    if koniec_hry:
        window.fill(BIELA)
        text = hra_font.render(koniec_hry_vypis, True, CIERNA)
        tlacidlo_vypisanie = text.get_rect(center=(SIRKA//2,VYSKA//2))
        window.blit(text, tlacidlo_vypisanie)
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()



