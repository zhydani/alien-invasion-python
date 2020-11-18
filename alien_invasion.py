import sys
import pygame

from settings import Settings


def run_game():
    # inicializa o jogo e cria um objeto para tela
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    bg_color = (230, 230, 230)

    # Inicia o laço principal do jogo
    while True:
        # observa eventos de teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # redesenha a tela a cada passagem pelo laco
        screen.fill(ai_settings.bg_color)

        # deixa a tela mais recente visível
        pygame.display.flip()


run_game()
