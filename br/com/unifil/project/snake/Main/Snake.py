import pygame
from pygame.locals import *

def main():
    # Iniciar o pygame
    pygame.init()

    # Tela do jogo
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Snake")

    # Tamanho da cobra padrão
    snake = [(200, 200), (210, 200), (220, 200), (230, 200)]
    # Quantos de pixels ocupa cada tupla da cobra
    snake_skin = pygame.Surface((10, 10))
    # Cor da cobra
    snake_skin.fill((255, 255, 255))

    # Quantos de pixel ocupa cada maçã
    apple = pygame.Surface((10, 10))
    # Cor da maçã
    apple.fill((255, 0, 0))

    # Quantos de pixel ocupa cada maçã
    apple2 = pygame.Surface((10, 10))
    # Cor da maçã
    apple2.fill((0, 255, 0))

    # Direção da cobra
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    direcao = LEFT

    clock = pygame.time.Clock()

    while True:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    direcao = UP
                if event.key == K_DOWN:
                    direcao = DOWN
                if event.key == K_RIGHT:
                    direcao = RIGHT
                if event.key == K_LEFT:
                    direcao = LEFT

        if direcao == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if direcao == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if direcao == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if direcao == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])

        # Faz com que a cobra se movimente.
        # as tuplas(corpo da cobra) vão se movimentando sempre na posição anterior onde a tupla da frente estava
        # ocupando antes de se movimentar
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])

        # Limpar a tela
        screen.fill((0, 0, 0))

        screen.blit(apple, (50, 50))
        screen.blit(apple2, (100, 500))

        for posicao in snake:
            screen.blit(snake_skin, posicao)



        pygame.display.update()
        #pygame.display.flip()

if __name__ == "__main__":
    # Chamar a função main
    main()