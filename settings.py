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
