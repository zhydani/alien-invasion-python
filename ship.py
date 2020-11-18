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

    def blitme(self):
        # desenha a espaconave em sua posicao atual
        self.screen.blit(self.image, self.rect)
