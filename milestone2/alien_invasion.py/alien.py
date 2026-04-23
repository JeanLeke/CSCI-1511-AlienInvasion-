"""
Program: Alien Invasion Game
Author: Jean Lekefua Fombindia
Date: 22 April 2026
Code:
Purpose: 

"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):

        super().__init__()
        self.screen = ai_game.screen 
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.direction = 1

    def update(self):
        """Movement of the alien left or right."""

        self.x += self.settings.alien_speed * self.direction
        self.rect.x = self.x

        if self.rect.right >= self.screen.get_rect().right:
            self.direction = -1
        elif self.rect.left <= 0:
            self.direction = 1 