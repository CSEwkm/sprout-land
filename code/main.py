#! /usr/bin/env python3
'''pygame 主框架
'''

import pygame
from config import settings
class Game:
    '''游戏初始化、主循环
    '''
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption(settings.CAPTION)
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        # 计算自上次调用以来已过去多少毫秒            
        dt = self.clock.tick(settings.FPS) / 1000
        
        pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()