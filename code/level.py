'''不同阶段或关卡
'''
import pygame

class Level:
    def __init__(self, name, map) -> None:
        self.name = name
        self.map = map
        self.display_