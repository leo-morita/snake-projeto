import pygame
# Iniciar o pygame
pygame.init()

# Pontuação do jogo
pontos = 0

# Tela do jogo
largura_tela = 600
altura_tela = 600
screen = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Snake")



# Background da tela
background = pygame.image.load("background600x600.jpg")
screen.blit(background, (0, 0))
pygame.display.update()

# Subtela do jogo
x = 200
y = 500
subsurface = pygame.Surface((largura_tela, altura_tela))
subsurface = subsurface.subsurface(pygame.Rect(0, 0, x, y))
subsurface.fill((255,255,255))
screen.blit(subsurface, (0, 0))
pygame.display.update()

running = True

while running:
    # Manipulação de eventos, obtém todos os eventos da fila de eventos
    for event in pygame.event.get():
        # Só faça algo se o evento for do tipo QUIT
        if event.type == pygame.QUIT:
            # Mude o valor para False, para sair do main loop
            running = False