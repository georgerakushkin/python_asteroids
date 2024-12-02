import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from shot import Shot

clock = pygame.time.Clock()
dt = 0
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shot_group = pygame.sprite.Group()


Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (updatable, drawable, shot_group)

asteroid_field = AsteroidField()

def main():
    pygame.init()

    obj_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update game state
        delta = clock.tick(60)
        dt = delta/1000
        
        for obj in updatable:
            obj.update(dt)
            
        for asteroid in asteroids:
            if asteroid.col_check(obj_player):
                print("Game over!")
                exit()
            # Check bullet collisions
            for shot in shot_group:
                if shot.col_check(asteroid):
                    asteroid.split()
                    shot.kill()
        
        # Draw everything
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()


if __name__=="__main__":
    main()

