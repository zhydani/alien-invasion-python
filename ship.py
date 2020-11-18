# -*- coding: utf-8 -*-
import pygame


class Ship():

    def __init__(self, screen):
        # inicializa a espaconave e define sua posicao inicial
        self.screen = screen

        # carrega a imagem da espaconave e ontem seu rect
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # inicia cad nova espaconave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # atualiza a posicao da espaco nave de acordo com a flag de movimento
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        # desenha a espaconave em sua posicao atual
        self.screen.blit(self.image, self.rect)
