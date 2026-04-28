"""
Program: Alien Invasion Game
Author: Jean Lekefua Fombindia
Date: 22 April 2026
Purpose:This file defines the Alien class used in the game.

"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Represents a single alien enemy that moves side to side."""

    def __init__(self, ai_game):
        """Create an alien instance and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen 
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.direction = 1

    def _update_aliens(self):
        """Update position of all aliens."""
        self._check_fleet_edges()
        self.aliens.update()

        if self.stats.game_active:
            if pygame.sprite.spritecollideany(self.ship, self.aliens):
                print("Ship hit!")
                self.stats.game_active = False
                pygame.mouse.set_visible(True)

        self._check_aliens_bottom()