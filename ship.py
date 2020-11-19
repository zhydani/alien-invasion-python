# -*- coding: utf-8 -*-
import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        # inicializa a espaconave e define sua posicao inicial
        self.screen = screen
        self.ai_settings = ai_settings

        # carrega a imagem da espaconave e ontem seu rect
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # inicia cad nova espaconave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # armazena um valor decimal para o centro da nave
        self.center = float(self.rect.centerx)

        # flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # atualiza a posicao da espaco nave de acordo com a flag de movimento
        # atualiza o valor do centro da nave e nao o retangulo
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # atualiza o objeto rect de acordo com o self.center
        self.rect.centerx = self.center

    def blitme(self):
        # desenha a espaconave em sua posicao atual
        self.screen.blit(self.image, self.rect)
