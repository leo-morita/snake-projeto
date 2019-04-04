import pygame, random
from pygame.locals import *

def colisao(obj1, obj2):
    return (obj1[0] == obj2[0]) and (obj1[1] == obj2[1])

def text_objects(font, text, color, text_center):
    rendered = font.render(text, True, color)
    return rendered, rendered.get_rect(center=text_center)

def main():
    # Iniciar o pygame
    pygame.init()

    # Tela do jogo
    largura_tela = 600
    altura_tela = 600
    screen = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Snake")

    # Background da tela
    background = pygame.image.load("background600x600.jpg")
    screen.blit(background, (0, 0))
    pygame.display.update()

    # Tamanho da cobra padrão
    snake = [(200, 200), (210, 200), (220, 200), (230, 200)]
    # Quantos de pixels ocupa cada tupla da cobra
    snake_skin = pygame.Surface((10, 10))
    # Cor da cobra
    snake_skin.fill((255, 255, 255))

    # Quantos de pixel ocupa cada maçã
    apple1_posicao = (50, 50)
    apple = pygame.Surface((10, 10))
    # Cor da maçã
    apple.fill((255, 0, 0))

    # Quantos de pixel ocupa cada maçã
    apple2_posicao = (100, 500)
    apple2 = pygame.Surface((10, 10))
    # Cor da maçã
    apple2.fill((255, 0, 0))

    # Quantos de pixel ocupa cada maçã
    apple3_posicao = (590, 200)
    apple3 = pygame.Surface((10, 10))
    # Cor da maçã
    apple3.fill((255, 0, 0))

    # Direção da cobra
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    direcao = LEFT

    # FPS do jogo
    clock = pygame.time.Clock()

    # Mensagem na tela
    pygame.font.init()
    fonte_padrao = pygame.font.get_default_font()
    fonte_game_over = pygame.font.SysFont(fonte_padrao, 50)

    # Variável para controlar o fluxo de execução do jogo
    running = True
    while running:
        # FPS setado para 10 - Velocidade da movimentação do jogo
        clock.tick(10)
        for event in pygame.event.get():
            # Para fechar o jogo, basta clicar no botão 'X' da tela, ou apertar a tecla 'ESC'
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            # Configuração das teclas para movimentar a cobra
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    direcao = UP
                if event.key == K_DOWN:
                    direcao = DOWN
                if event.key == K_RIGHT:
                    direcao = RIGHT
                if event.key == K_LEFT:
                    direcao = LEFT

        # Método que faz com que a cobra se movimente.
        if direcao == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if direcao == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if direcao == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if direcao == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])

        # Método condicional que verifica a colisão da cobra com a maçã
        if colisao(snake[0], apple1_posicao):
            if apple.get_at((0, 0)) == (255, 0, 0, 255) and apple.get_alpha() != 0:
                snake.append((0, 0))
                snake_skin.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                apple.set_alpha(0)

        if colisao(snake[0], apple2_posicao) and apple2.get_alpha() != 0:
            if apple2.get_at((0, 0)) == (255, 0, 0, 255) and apple2.get_alpha() != 0:
                snake.append((0, 0))
                snake_skin.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                apple2.set_alpha(0)

        if colisao(snake[0], apple3_posicao) and apple3.get_alpha() != 0:
            if apple3.get_at((0, 0)) == (255, 0, 0, 255):
                snake.append((0, 0))
                snake_skin.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                apple3.set_alpha(0)

        # Método condicional que verifica a colisão da cobra contra o seu próprio corpo
        #if colisao(snake[0], ):
            #print("Entrou na condicional")
            #running = False

        # Método condicional que verifica a colisão da cobra com a borda da tela
        # Borda esquerda e direita
        if snake[0][0] < 0 or snake[0][0] >= 599:
            #texto = fonte_game_over.render('O jogo acabou!', 1, (255, 255, 255))

            #screen.blit.center(texto, (largura_tela/2, altura_tela/2))
            screen.blit(*text_objects(fonte_game_over, 'O jogo acabou!', (255, 255, 255), screen.get_rect().center))
            pygame.display.update()
            clock.tick(0.5)
            running = False

        # Borda de cima e de baixo
        if snake[0][1] < 0 or snake[0][1] >= 599:
            running = False

        # as tuplas(corpo da cobra) vão se movimentando sempre na posição anterior onde a tupla da frente estava
        # ocupando antes de se movimentar
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])

        # Limpar a tela
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        # Plotando as maçãs na tela
        screen.blit(apple, apple1_posicao)
        screen.blit(apple2, apple2_posicao)
        screen.blit(apple3, apple3_posicao)

        # Plotando a cobra na tela
        for posicao in snake:
            screen.blit(snake_skin, posicao)

        pygame.display.update()
        #pygame.display.flip()

if __name__ == "__main__":
    # Chamar a função main
    main()