"""
Program: Alien Invasion Game
Author: Jean Lekefua Fombindia
Date: 13 April 2026
Purpose:is to store all game settings

"""

class Settings:
    """Holds all the configuration values for the Alien Invasion game."""

    def __init__(self):
        """Set up default values for display, movement, and gameplay."""

        self.screen_width = 1200
        self.screen_height = 800

        self.bg_color = (230, 230, 230)
        self.frame_rate = 60

        self.ship_speed = 8

        self.bullet_speed = 2
        self.bullet_width = 3   
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        self.bullets_allowed = 20

        self.alien_speed = 1
        self.fleet_direction = 1