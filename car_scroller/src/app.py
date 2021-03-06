import pygame
import time
import sys
from pygame.locals import *
from random import randint

# Initialize the program
pygame.init()

# Assign the game FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Set up game color options
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
# HIGH_SCORE = load_history()

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("car_scroller/src/AnimatedStreet.png")

# Set up the display with a caption
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Fun With Pygame")


# Create the classes for enemy and player
# Should inherit from pygame.sprite.Sprite
# Create Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car_scroller/src/Enemy.png")
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center=(randint(30, 370), 0))

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (randint(30, 370), 0)


# Create Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car_scroller/src/Player.png")
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect(center=(150, 500))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


# Instantiate Player and Enemy
player = Player()
enemy = Enemy()


# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(enemy)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)


# Add a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1500)


# Game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            if SPEED <= 12:
                SPEED += 2

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Move and re-draw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Runs if collision between player and enemy
    if pygame.sprite.spritecollideany(player, enemies):
        pygame.mixer.Sound('car_scroller/src/crash.wav').play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
