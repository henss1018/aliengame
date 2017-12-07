class Settings():
    """存储所有设置信息"""

    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        #飞船移动速度
        self.ship_speed_factor = 1.8

        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #移动方向，1表示右移，-1表示左移
        self.fleet_direction = 1