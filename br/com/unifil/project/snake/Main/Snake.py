import pygame

print("Welcome to Snake-project")

def main():
    # Iniciar o pygame
    pygame.init()

    # Carregar e definir o logotipo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("movement")

    # Crie uma superfície na tela que tenha o tamanho de 500 x 500
    screen_width = 500
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Carregar imagem
    image = pygame.image.load("imagem01.jpg")

    # Esta função, funciona em algumas imagens, caso esta imagem não tem um valor alpha, aí faz com que tire as
    # bordas da imagem selecionada
    #image.set_colorkey((255, 0, 255))

    # Faz com que a imagem fique transparente
    image.set_alpha(120)

    # Com esta função, faz com que o background do cenário fique tudo branco
    # screen.fill((255, 255, 255))

    background = pygame.image.load("background.jpg")
    # blit - O que faz é copiar os pixels da superfície da imagem para a superfície da tela
    screen.blit(background, (0, 0))

    # Define a posição da imagem
    x_pos = 50
    y_pos = 50

    # Quantos pixels nós movemos o nosso quadro
    step_x = 10
    step_y = 10

    # Copia os pixels da imagem na tela
    #screen.blit(image, (x_pos, y_pos))
    screen.blit(image, (50, 50))

    # Atualizar a tela
    pygame.display.flip()

    # Clock para controlar o FPS depois
    clock = pygame.time.Clock()

    # Defina uma variável para controlar o loop principal
    running = True

    # Main loop
    while running:
        # Manipulação de eventos, obtém todos os eventos da fila de eventos
        for event in pygame.event.get():
            # Só faça algo se o evento for do tipo QUIT
            if event.type == pygame.QUIT:
                # Mude o valor para False, para sair do main loop
                running = False

            # Verifique a tecla e verifique se foi Esc
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # Verifique se a imagem ainda está na tela, se não, mudar de direção
        if x_pos > screen_width - 64 or x_pos < 0:
            step_x = -step_x
        if y_pos > screen_height - 64 or y_pos < 0:
            step_y = -step_y

        # Atualizar a posição da imagem
        x_pos += step_x  # Mover para a direita
        y_pos += step_y  # Mover para baixo

        # Agora, copia todos os pixels(blit) da imagem na tela
        #screen.blit(image, (x_pos, y_pos))
        screen.blit(image, (50, 50))

        # Atualiza a tela
        pygame.display.flip()

        # isso vai diminuir a velocidade para 10 fps, para que você possa assisti-lo,
        # caso contrário, seria executado muito rápido
        clock.tick(10)

# Executar a função principal somente se este módulo for executado como o script principal
# (se você importar isso como um módulo, nada será executado)
if __name__=="__main__":
    # Chamar a função main
    main()