import pygame

import random


class Entity(pygame.sprite.Sprite):
    def __init__(self, settings, size, color):
        super(Entity, self).__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        #     center=(
        #         random.randint(settings.width + 20, settings.width + 100),
        #         random.randint(0, settings.height),
        #     )
        # self.speed = random.randint(5, 20)


class Entities(pygame.sprite.Group):
    def __init__(self):
        super(Entities, self).__init__()
        return None

    def addEntity(self, entity):
        self.add(entity)
        return 0