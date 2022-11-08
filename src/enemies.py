import pygame

import random


class BasicEnemy(pygame.sprite.Sprite):
    def __init__(self, settings, size, color):
        super(BasicEnemy, self).__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect()