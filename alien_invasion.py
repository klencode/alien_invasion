import sys

import pygame

from settings import Settings

from ship import ship

class AlienInvasion:
    """Overall class to manage games assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.int()
        
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        # Set the background color.
        # self.bg_color = (230, 230, 230)

        # self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        self.ship = ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            
    # Redraw the screen during each pass through the loop.
    # Watch for keyboard and mouse events.
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        
            
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

            # Make the most recently drawn screen visible.
        pygame.display.flip()
            

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
