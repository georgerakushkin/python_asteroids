import pygame
import random
from constants import *
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            random_angle = random.uniform(20,50)
            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)

            x,y = self.position
            # Instantiate two new asteroids using x, y, and the new_radius
            new_asteroid1 = Asteroid(x, y, new_radius)
            new_asteroid2 = Asteroid(x, y, new_radius)
            new_asteroid1.velocity = new_velocity1 * 1.2
            new_asteroid2.velocity = new_velocity2 * 1.2


        
