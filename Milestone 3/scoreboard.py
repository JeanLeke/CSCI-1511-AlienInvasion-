"""
Program: Alien Invasion Game
Author: Jean Lekefua Fombindia
Date: 27 April 2026
Purpose: is to display important game information 
to the player while the game is running. 

"""

import pygame

class Scoreboard:
    """Show score."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.stats = ai_game.stats
        self.font = pygame.font.SysFont(None, 48)
        self.color = (30, 30, 30)

        self.prep_score()

    def prep_score(self):
        self.image = self.font.render(str(self.stats.score), True, self.color)
        self.rect = self.image.get_rect()
        self.rect.right = self.screen.get_rect().right - 20
        self.rect.top = 20

    def show_score(self):
        self.screen.blit(self.image, self.rect) 