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
    screen = pygame.display.set_mode((500,500))

    # Defina uma variável para controlar o loop principal
    running = True

    # Main loop
    while running:
        # Manipulação de eventos, obtém todos os eventos da fila de eventos
        for event in pygame.event.get():
            # Carregar imagem
            image = pygame.image.load("imagem01.jpg")
            background = pygame.image.load("background.jpg")



            # Com esta função, faz com que o background do cenário fique tudo branco
            #screen.fill((255, 255, 255))

            # blit - O que faz é copiar os pixels da superfície da imagem para a superfície da tela
            screen.blit(background, (0, 0))
            image.set_alpha(128)
            #image.set_colorkey((255, 0, 255))
            screen.blit(image, (50, 50))
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