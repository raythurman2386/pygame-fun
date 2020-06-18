import pygame
from constants import *
from ship import Player, Enemy

# Game loop
class Game:
    def __init__(self, run=True, FPS=60, level=1, lives=5):
        self.run = run
        self.FPS = FPS
        self.level = level
        self.lives = lives
        self.main_font = pygame.font.SysFont("comicsans", 50)
        self.clock = pygame.time.Clock()
        self.player = Player(300, 650)
        # self.enemy = Enemy(300, 100)
        self.player_vel = 5

    def redraw_window(self):
        WIN.blit(BACKGROUND, (0, 0))
        # Draw text
        lives_label = self.main_font.render(f"Lives: {self.lives}", 1, (255, 255, 255))
        level_label = self.main_font.render(f"Level: {self.level}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        self.player.draw(WIN)
        # self.enemy.draw(WIN)

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

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and self.player.x + self.player_vel > 0:  # Left
                self.player.x -= self.player_vel
            if keys[pygame.K_d] and self.player.x + self.player_vel + 50 < WIDTH:  # Right
                self.player.x += self.player_vel
            if keys[pygame.K_w] and self.player.y + self.player_vel > 0:  # Up
                self.player.y -= self.player_vel
            if keys[pygame.K_s] and self.player.y + self.player_vel + 50 < HEIGHT: # Down
                self.player.y += self.player_vel
