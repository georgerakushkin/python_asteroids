import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    SHOT_RADIUS = 5
    
    def __init__(self, x, y, radius=5):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        self.shot_radius = self.SHOT_RADIUS
        self.radius = self.SHOT_RADIUS

    def draw(self, surface):
        pygame.draw.circle(surface, (255,255,255), self.position, self.shot_radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)


