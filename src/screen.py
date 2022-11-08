import pygame


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
