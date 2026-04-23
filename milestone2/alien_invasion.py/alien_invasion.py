"""
Program: Alien Invasion Game
Author: Jean Lekefua Fombindia
Date: 22 April 2026
Code: https://github.com/RedBeard41/alien_Invasion_starter.git
Purpose: Is to modify the game to change the ship's orientation and movement.

"""

import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """The main controller for the game. Handles setup, updates, and gameplay flow."""
   
    def __init__(self):
        """Set up the game window, settings, and all starting objects."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()


        self._create_fleet()

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Keep the game running by looping through updates and screen refreshes."""
        while True:
            self._check_events()

            self.ship.update()
            self.aliens.update()

            self._update_bullets()
            self._check_bullet_alien_collisions() 
            self._check_aliens_position()

            self._update_screen()

            self.clock.tick(self.settings.frame_rate)

    def _check_events(self):
        """Watch for keyboard and window events and respond accordingly."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """React when a key is pressed (movement, shooting, or quitting)."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Stop movement when the player releases a key."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_fleet(self):
        """Build a grid of aliens that fills part of the screen."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 1 * alien_width


            current_x = alien_width
            current_y += 1 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create one alien and place it at a specific location."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


    def _check_bullet_alien_collisions(self):
        """Remove aliens and bullets when they collide, and respawn fleet if needed."""
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if len(self.aliens) == 0:
            self._create_fleet()

    def _check_aliens_position(self):
        """Check if aliens hit the ship or reach the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.colliderect(self.ship.rect):
                self._reset_game()

        if alien.rect.bottom >= self.settings.screen_height:
            self._reset_game()


    def _reset_game(self):
        """Clear everything and restart positions after a hit or loss."""
        self.bullets.empty()
        self.aliens.empty()
        self._create_fleet()
        self.ship.rect.midbottom = self.screen.get_rect().midbottom


    def _fire_bullet(self):
        """Shoot a bullet if the limit hasn't been reached."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Move bullets upward and remove any that go off-screen."""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self): 
        """Draw all game elements and refresh the display."""
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    """Launch the game when this file is run directly."""
    ai = AlienInvasion()
    ai.run_game()