# -*- coding: utf-8 -*-
import sys
import pygame


def check_events(ship):
    # responde a eventos de pressionamento de teclas e de mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move a nave para a direita
                ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship):
    # atualiza as imagens na tela e alterna para a nova tela
    # redesenha a tela a cada passagem do laco
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # deixa a tela mais recente visível
    pygame.display.flip()
