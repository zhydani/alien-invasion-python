import sys

import pygame


def run_game():
    # inicializa o jogo e cria um objeto para tela
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    bg_color = (230, 230, 230)

    # Inicia o laço principal do jogo
    while True:
        # observa eventos de teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # redesenha a tela a cada passagem pelo laco
        screen.fill(bg_color)

        # deixa a tela mais recente visível
        pygame.display.flip()


run_game()
