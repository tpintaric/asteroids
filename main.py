import pygame
import sys
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import *

pygame.init()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
           if asteroid.collision(player):
              print("Game Over!") 
              sys.exit(1)
              
        #player.update(dt)
        screen.fill("black")
        #drawable.draw(screen)
        for sprite in drawable:
            sprite.draw(screen)

        #player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

