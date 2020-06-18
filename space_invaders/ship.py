import pygame
from random import choice
from constants import *

# Ship class to create Player and Enemy Ships
class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health


class Enemy(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = choice([RED_SPACE_SHIP, GREEN_SPACE_SHIP, BLUE_SPACE_SHIP])
        self.laser_img = self.get_laser()
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def get_laser(self):
        if self.ship_img == RED_SPACE_SHIP:
            self.laser_img = RED_LASER
        elif self.ship_img == GREEN_SPACE_SHIP:
            self.laser_img = GREEN_LASER
        elif self.ship_img == BLUE_SPACE_SHIP:
            self.laser_img = BLUE_LASER
