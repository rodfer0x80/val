import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

import random


class Game():
    def __init__(self, settings):
        self.settings = settings
        self.running = True
        return None

    def update(self, player):
        global QUIT, K_ESCAPE
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
            elif event.type == QUIT:
                self.running = False
        self.updatePlayer(player)
        return 0

    def updateEnemy(self, enemy):
        enemy.rect.move_ip(-enemy.speed, 0)
        if enemy.rect.right < 0:
            enemy.kill()

    def updatePlayer(self, player):
        global K_UP, K_DOWN, K_LEFT, K_RIGHT
        pressed_keys = pygame.key.get_pressed()
        step = 2
        if pressed_keys[K_UP]:
            if player.rect.y -(step) > 0:
                player.rect.move_ip(0, -(step))
        elif pressed_keys[K_DOWN]:
            if player.rect.y + step < self.settings.height:
                player.rect.move_ip(0, step)
        elif pressed_keys[K_LEFT]:
            if player.rect.x -(step) > 0:
                player.rect.move_ip(-(step), 0)
        elif pressed_keys[K_RIGHT]:
            if player.rect.x + step < self.settings.width:
                player.rect.move_ip(step, 0)
        return 0
