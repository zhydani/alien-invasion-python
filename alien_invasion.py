# -*- coding: utf-8 -*-
import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # inicializa o jogo e cria um objeto para tela
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    # cria um grupo no qual serao armazenados os projeteis
    bullets = Group()

    bg_color = (230, 230, 230)

    # Inicia o laco principal do jogo
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # apaga projetei s que desaparecem
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
