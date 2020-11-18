import pygame


class Ship():

    def __init__(self, screen):
        # inicializa a espaconave e define sua posicao inicial
        self.screen = screen

        # carrega a imagem da espaconave e ontem seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
