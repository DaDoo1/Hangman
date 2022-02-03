
import pygame
pygame.init()

#nastavenia okna
window = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Hangman")
logo = pygame.image.load("001-hangman.png")
pygame.display.set_icon(logo)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
