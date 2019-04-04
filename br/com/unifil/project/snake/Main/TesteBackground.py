import pygame, random
from pygame.locals import *

# Iniciar o pygame
pygame.init()

# Tela do jogo
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")

# Background da tela
background = pygame.image.load("background600x600.jpg")
screen.blit(background, (0, 0))

pygame.display.update()

running = True

while running:
    # Manipulação de eventos, obtém todos os eventos da fila de eventos
    for event in pygame.event.get():
        # Só faça algo se o evento for do tipo QUIT
        if event.type == pygame.QUIT:
            # Mude o valor para False, para sair do main loop
            running = False

pygame.display.update()