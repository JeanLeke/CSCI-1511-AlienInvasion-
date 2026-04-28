"""
Program: Alien Invasion Game
Author: Jean Lekefua Fombindia
Date: 13 April 2026
Purpose: Is to handles bullets fired from ship 

"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Represents a single bullet fired from the player's ship."""
    def __init__(self, ai_game):
        """Create a bullet and position it at the front of the ship."""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midtop = ai_game.ship.rect.midtop

    def update(self):
        """Move the bullet upward each frame."""
        self.rect.y -= self.settings.bullet_speed

    def draw_bullet(self):
        """Draw the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)