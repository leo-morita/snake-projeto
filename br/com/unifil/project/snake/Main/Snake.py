import pygame

print("Welcome to Snake-project")

def main():
    # Iniciar o pygame
    pygame.init()

    # Carregar e definir o logotipo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # Crie uma superfície na tela que tenha o tamanho de 500 x 500
    screen_width = 500
    screen_height = 500
    screen = pygame.display.set_mode((screen_width,screen_height))

    # Defina uma variável para controlar o loop principal
    running = True

    # Main loop
    while running:
        # Manipulação de eventos, obtém todos os eventos da fila de eventos
        for event in pygame.event.get():
            # Define a posição da imagem
            x_pos = 50
            y_pos = 50

            # Quantos pixels nós movemos o nosso quadro
            step_x = 10
            step_y = 10

            # Verifique se a imagem ainda está na tela, se não, mudar de direção
            if x_pos > screen_width-64 or x_pos < 0:
                step_x = -step_x
            if y_pos > screen_height-64 or y_pos < 0:
                step_y = -step_y

            # Atualizar a posição da imagem
            x_pos += step_x # Mover para a direita
            y_pos += step_y # Mover para baixo

            # Carregar imagem
            image = pygame.image.load("imagem01.jpg")
            background = pygame.image.load("background.jpg")

            # Com esta função, faz com que o background do cenário fique tudo branco
            #screen.fill((255, 255, 255))

            # blit - O que faz é copiar os pixels da superfície da imagem para a superfície da tela
            screen.blit(background, (0, 0))

            # Faz com que a imagem fique transparente
            image.set_alpha(128)

            # Esta função, funciona em algumas imagens, caso esta imagem não tem um valor alpha, aí faz com que tire as
            # bordas da imagem selecionada
            #image.set_colorkey((255, 0, 255))

            #screen.blit(image, (50, 50))
            screen.blit(image, (x_pos, y_pos))

            # Atualizar a tela
            pygame.display.flip()

            # Só faça algo se o evento for do tipo QUIT
            if event.type == pygame.QUIT:
                # Mude o valor para False, para sair do main loop
                running = False

# Executar a função principal somente se este módulo for executado como o script principal
# (se você importar isso como um módulo, nada será executado)
if __name__=="__main__":
    # Chamar a função main
    main()