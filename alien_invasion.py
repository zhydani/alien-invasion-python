# -*- coding: utf-8 -*-
import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # inicializa o jogo e cria um objeto para tela
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    bg_color = (230, 230, 230)

    # Inicia o laço principal do jogo
    while True:
        # observa eventos de teclado e mouse
        gf.check_events()

        # redesenha a tela a cada passagem pelo laco
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # deixa a tela mais recente visível
        pygame.display.flip()


run_game()
