import pygame

print("Welcome to Snake-project")

def main():
    # Iniciar o pygame
    pygame.init()

    # Carregar e definir o logotipo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # Crie uma superfície na tela que tenha o tamanho de 240 x 180
    screen = pygame.display.set_mode((240,180))

    # Defina uma variável para controlar o loop principal
    running = True

    # Main loop
    while running:
        # Manipulação de eventos, obtém todos os eventos da fila de eventos
        for event in pygame.event.get():
