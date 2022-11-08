#!/usr/bin/env python3

import sys
import time
import random

import pygame
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


# Runner constants
class Screen:
    def __init__(self, settings):
        self.settings = settings
        return None
    
    def makeDisplay(self):
        self.display = pygame.display.set_mode([self.settings.width, self.settings.height])
        return self.display

    def updateDisplay(self):
        pygame.display.flip()
        return 0

    def drawBackground(self):
        self.display.fill((255, 255, 255))
        return 0

    def drawCharacters(self, characters):
        for character in characters:
            self.display.blit(character.surf, character.rect)
        return 0

    def drawEntities(self, entities):
        for entity in entities:
            self.display.blit(entity.surf, entity.rect)
        return 0


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


class BasicEnemy(pygame.sprite.Sprite):
    def __init__(self, settings, size, color):
        super(BasicEnemy, self).__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect()


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


class Characters(pygame.sprite.Group):
    def __init__(self):
        super(Characters, self).__init__()
        return None

    def addCharacter(character):
        self.add(character)
        return 0


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


class Settings:
    def __init__(self):
        self.width = 1440
        self.height = 1080
        return None


def main():
    pygame.init()

    settings = Settings()
    entities = Entities()
    characters = Characters()
    game = Game(settings)
    screen = Screen(settings)

    screen.makeDisplay()

    box = Entity(settings, (81, 81), (0, 0, 255))
    entities.add(box)

    player = Player()
    characters.add(player)

    enemy = BasicEnemy(settings, (49, 49), (255, 0, 0))
    characters.add(enemy)

    while game.running:
        game.update(player)
        screen.drawBackground()
        screen.drawEntities(entities)
        screen.drawCharacters(characters)

        screen.updateDisplay()
        
    pygame.quit()
    return 0


if __name__ == '__main__':
    sys.exit(main())
