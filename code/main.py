#! /usr/bin/env python3
'''pygame loop running
'''
import pygame
from config import settings
class Game:
    '''pygame setup
    '''
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption(settings.CAPTION)
        self.clock = pygame.time.Clock()
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        self.dt = 0
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # To Do
            # move something within dt
            # ...   
                     
            # flip() the display to put your work on screen
            pygame.display.flip()
            dt = self.clock.tick(settings.FPS) / 1000
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()