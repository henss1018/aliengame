# !python3

import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        #初始化屏幕
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船图片并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #将每艘飞船放置在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #根据移动标志移动飞船
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)