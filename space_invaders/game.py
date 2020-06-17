import pygame
import os
import sys
import random
from constants import *

# Game loop
class Game:
    def __init__(self, run=True, FPS=60, level=1, lives=5):
        self.run = run
        self.FPS = FPS
        self.level = level
        self.lives = lives
        self.main_font = pygame.font.SysFont("comicsans", 50)
        self.clock = pygame.time.Clock()

    def redraw_window(self):
        WIN.blit(BACKGROUND, (0, 0))
        # Draw text
        lives_label = self.main_font.render(f"Lives: {self.lives}", 1, (255, 255, 255))
        level_label = self.main_font.render(f"Level: {self.level}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        pygame.display.update()

    def quit_game(self):
        self.run = False

    def play(self):
        while self.run:
            self.clock.tick(self.FPS)
            self.redraw_window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
