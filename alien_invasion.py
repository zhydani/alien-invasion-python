# -*- coding: utf-8 -*-
import sys
import pygame

from settings import Settings
from ship import Ship
from alien import Alien
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
    aliens = Group()

    # cria a frotaa de alienigenas
    gf.create_fleet(ai_settings, screen, aliens)

    bg_color = (230, 230, 230)

    alien = Alien(ai_settings, screen)

    # Inicia o laco principal do jogo
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
