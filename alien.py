# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # uma classe que representa um único alienígena da frota 
    def __init__(self, ai_settings, screen):
        # inicializa o alienígena e define sua posicao inicial
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # carrega a imagem do alienigena e define seu atributo rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # inicia cada novo alienigena proximo a partre superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # armazena a posicao exata do alienigena
        self.x = float(self.rect.x)
    
    def blitme(self):
        # desenha o alienigena em sua posicao atual 
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Move o alienigena para a direita
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x