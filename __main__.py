#!/usr/bin/env python3


from src.screen import Screen
from src.settings import Settings
from src.game import Game
from src.entities import Entities, Entity
from src.characters import Characters
from src.player import Player
from src.enemies import BasicEnemy


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
