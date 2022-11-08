import pygame

import random


class Player(pygame.sprite.Sprite):
    def __init__(self, size=(49, 49), color=(0, 255, 0)):
        super(Player, self).__init__()
        self.updateStats(size, color)
        return None
    
    def updateStats(self, size=(49, 49), color=(0, 255, 0)):
        self.size = size
        self.color = color

        self.surf = pygame.Surface(self.size)
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect()
        return 0
