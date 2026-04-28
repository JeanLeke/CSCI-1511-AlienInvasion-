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
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard 

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
        self.stats = GameStats(self)
        self.game_active = False
        self.play_button = Button(self, "Play")
        self.sb = Scoreboard(self) 

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Keep the game running by looping through updates and screen refreshes."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._check_bullet_alien_collisions() 

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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

    def _check_play_button(self, mouse_pos):
        """Start a new game when Play is clicked."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.stats.game_active:

            self.stats.reset_stats()
            self.stats.game_active = True
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()

            pygame.mouse.set_visible(False)
    def _create_fleet(self):
        """Build a grid of aliens that fills part of the screen."""
        alien = Alien(self)

        alien_width = alien.rect.width
        alien_height = alien.rect.height

        screen_width = self.settings.screen_width
        number_aliens_x = screen_width // (2 * alien_width)
        number_rows = 4

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):

                alien = Alien(self)
                alien.x = alien_width + 2 * alien_width * alien_number
                alien.rect.x = alien.x
                alien.rect.y = alien_height + 2 * alien_height * row_number

                self.aliens.add(alien)

    def _create_alien(self, x):
        """Create one alien and place it at a specific location."""
        alien = Alien(self)
        alien.x = x
        alien.rect.x = x
        self.aliens.add(alien)



    def _check_bullet_alien_collisions(self):
        """Remove aliens and bullets when they collide, and respawn fleet if needed."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += 10 * len(aliens)
                self.sb.prep_score()

        if not self.aliens:
            self._create_fleet() 

    def _check_aliens_position(self):
        """Check if aliens hit the ship or reach the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.colliderect(self.ship.rect) or \
                alien.rect.bottom >= self.settings.screen_height:
            
                self._reset_game()  
                self.stats.game_active = False
                pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens hit bottom of screen."""
        screen_rect = self.screen.get_rect()

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                print("Alien reached bottom!")
                self.stats.game_active = False
                pygame.mouse.set_visible(True)
                break

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

    def _update_aliens(self):
        """Update position of all aliens.""" 
        self.aliens.update()

        if self.stats.game_active:
            if pygame.sprite.spritecollideany(self.ship, self.aliens):
                print("Ship hit!")
                self.stats.game_active = False
                pygame.mouse.set_visible(True)

        self._check_aliens_bottom()

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
        self.sb.show_score()

        if not self.stats.game_active: 
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    """Launch the game when this file is run directly."""
    ai = AlienInvasion()
    ai.run_game()