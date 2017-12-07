# !python3

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """单个外星人类"""
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人最初都在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人正确位置
        self.x = float(self.rect.x)


    def update(self):
        """向右移动外星人"""
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)