import pygame
import random
from constants import *
from ship import Player, Enemy, collide

# Game loop


class Game:
    def __init__(self, run=True, FPS=60, level=0, lives=5):
        # Minor game Setup items
        self.run = run
        self.FPS = FPS
        self.level = level
        self.lives = lives
        self.main_font = pygame.font.SysFont("comicsans", 50)
        self.clock = pygame.time.Clock()
        self.lost = False
        self.loss_count = 0
        # Player items
        self.player = Player(300, 650)
        self.player_vel = 5
        # Enemy Items
        self.enemies = []
        self.wave_length = 5
        self.enemy_vel = 1
        # Lasers Velocity
        self.laser_vel = 5

    def redraw_window(self):
        WIN.blit(BACKGROUND, (0, 0))
        # Draw text
        lives_label = self.main_font.render(
            f"Lives: {self.lives}", 1, (255, 255, 255))
        level_label = self.main_font.render(
            f"Level: {self.level}", 1, (255, 255, 255))

        # Draw the labels
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        # Draw the Ships
        for enemy in self.enemies:
            enemy.draw(WIN)
        self.player.draw(WIN)

        if self.lost:
            lost_lable = self.main_font.render(
                "You lost!! :(", 1, (255, 255, 255))
            WIN.blit(lost_lable, (WIDTH/2 - lost_lable.get_width()/2, 350))

        # updated the game display
        pygame.display.update()

    def quit_game(self):
        self.run = False

    def check_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

    def check_key_press(self, keys):
        if keys[pygame.K_a] and self.player.x + self.player_vel > 0:  # Left
            self.player.x -= self.player_vel
        if keys[pygame.K_d] and self.player.x + self.player_vel + self.player.get_width() < WIDTH:  # Right
            self.player.x += self.player_vel
        if keys[pygame.K_w] and self.player.y + self.player_vel > 0:  # Up
            self.player.y -= self.player_vel
        if keys[pygame.K_s] and self.player.y + self.player_vel + self.player.get_height() < HEIGHT:  # Down
            self.player.y += self.player_vel
        if keys[pygame.K_SPACE]:
            self.player.shoot()
        if keys[pygame.K_ESCAPE]:
            self.quit_game()

    def enemy_actions(self):
        for enemy in self.enemies[:]:
            enemy.move(self.enemy_vel)
            enemy.move_lasers(self.laser_vel, self.player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, self.player):
                self.player.health -= 10
                self.enemies.remove(enemy)

            if enemy.y + enemy.get_height() > HEIGHT:
                self.lives -= 1
                self.enemies.remove(enemy)

    def generate_enemies(self):
        if len(self.enemies) == 0:
            self.level += 1
            self.wave_length += 5
            for i in range(self.wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-50),
                              random.randrange(-1500, -100))
                self.enemies.append(enemy)

    def play(self):
        while self.run:
            self.clock.tick(self.FPS)
            self.redraw_window()

            if self.lives <= 0 or self.player.health <= 0:
                self.lost = True
                self.loss_count += 1

            if self.lost:
                if self.loss_count > self.FPS * 3:
                    self.run = False
                else:
                    continue

            self.generate_enemies()
            self.check_quit()
            keys = pygame.key.get_pressed()
            self.check_key_press(keys)
            self.enemy_actions()
            self.player.move_lasers(-self.laser_vel, self.enemies)
