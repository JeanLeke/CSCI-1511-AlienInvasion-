"""
Program: Alien Invasion Game
Author: Jean Lekefua Fombindia
Date: 13 April 2026
Purpose: Is to control the player ship. 

"""

import pygame

class Ship:
    """Represents the player’s ship and handles its movement."""
    def __init__(self, ai_game):
        """Initialize the ship and place it at the bottom center of the screen."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship’s position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed

    def blitme(self):
        """Draw the ship at its current position on the screen."""
        self.screen.blit(self.image, self.rect)
