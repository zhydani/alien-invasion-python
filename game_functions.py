# -*- coding: utf-8 -*-
import sys
import pygame


def check_keydown_events(event, ship):
    # responde a pressionamento de teclas
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    # responde a solturas de tecla
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    # responde a eventos de pressionamento de teclas e de mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    # atualiza as imagens na tela e alterna para a nova tela
    # redesenha a tela a cada passagem do laco
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # deixa a tela mais recente visível
    pygame.display.flip()
