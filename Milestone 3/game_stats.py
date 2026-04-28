"""
Program: Alien Invasion Game
Author: Jean Lekefua Fombindia
Date: 27 April 2026
Purpose: is to control how the game behaves at different moments.
"""

class GameStats:
    """Track score and lives."""

    def __init__(self, ai_game):
        """Initialize stats."""
        self.settings = ai_game.settings
        self.reset_stats()

        self.high_score = 0
        self.game_active = False

    def reset_stats(self):
        """Reset stats when game restarts."""
        self.ships_left = 3
        self.score = 0 