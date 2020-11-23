# -*- coding: utf-8 -*-
class Settings():
    # uma classe para armazenar todas as configuracoes do jogo

    def __init__(self):
        # inicializa as configuracoes do jogo
        # config de tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # config da spaceship
        self.ship_speed_factor = 1.5
        # config dos projeteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3
        # config dos alienigenas
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction igual a 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1
