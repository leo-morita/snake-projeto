import pygame
from pygame.locals import *

def colisao(snake, apple):
    return (snake[0] == apple[0]) and (snake[1] == apple[1])

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
    apple_posicao = (50, 50)
    apple = pygame.Surface((10, 10))
    # Cor da maçã
    apple.fill((255, 0, 0))

    # Quantos de pixel ocupa cada maçã
    apple2 = pygame.Surface((10, 10))
    # Cor da maçã
    apple2.fill((255, 0, 0))

    # Direção da cobra
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    direcao = LEFT

    clock = pygame.time.Clock()

    running = True

    while running:
        clock.tick(10)
        for event in pygame.event.get():
            # Para fechar o jogo, basta clicar no botão 'X' da tela, ou apertar a tecla 'ESC'
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    direcao = UP
                if event.key == K_DOWN:
                    direcao = DOWN
                if event.key == K_RIGHT:
                    direcao = RIGHT
                if event.key == K_LEFT:
                    direcao = LEFT

        # Faz com que a cobra se movimente.
        if direcao == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if direcao == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if direcao == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if direcao == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])

        if colisao(snake[0], apple_posicao):
            #if apple.get_colorkey() == (0, 0, 0):
                #snake.append((0, 0))
            if apple.get_at((0, 0)) == (255, 0, 0, 255):
                snake.append((0, 0))
                snake_skin.fill((255, 0, 0))
            apple.fill((0, 0, 0))


        # as tuplas(corpo da cobra) vão se movimentando sempre na posição anterior onde a tupla da frente estava
        # ocupando antes de se movimentar
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])

        # Limpar a tela
        screen.fill((0, 0, 0))

        #screen.blit(apple_posicao[0], (apple_posicao[0][0], apple_posicao[0][1]))
        #screen.blit(apple_posicao[1], (80, 80)))
        screen.blit(apple, apple_posicao)
        screen.blit(apple2, (100, 500))

        for posicao in snake:
            screen.blit(snake_skin, posicao)



        pygame.display.update()
        #pygame.display.flip()

if __name__ == "__main__":
    # Chamar a função main
    main()