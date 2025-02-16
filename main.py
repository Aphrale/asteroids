import sys
import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    dt = 0

    shot_grp = pygame.sprite.Group()
    asteroid_grp = pygame.sprite.Group()
    updatable_grp = pygame.sprite.Group()
    drawable_grp = pygame.sprite.Group()
    
    Player.containers = (updatable_grp, drawable_grp, shot_grp)
    Shot.containers = (updatable_grp, drawable_grp, shot_grp)
    Asteroid.containers = (asteroid_grp, updatable_grp, drawable_grp)
    AsteroidField.containers = updatable_grp
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
    
        dt = clock.tick(60) / 1000
    
        updatable_grp.update(dt)
    
    # Bullet-asteroid collisions
        for asteroid in asteroid_grp:
            for shot in shot_grp:
                if asteroid.collision(shot):
                    asteroid.kill()
                    shot.kill()
    
    # Player-asteroid collision using sprite groups
        if pygame.sprite.spritecollideany(player, asteroid_grp):
            print("Game Over")
            pygame.quit()
            sys.exit()
    
        pygame.Surface.fill(screen, (0,0,0))
        for drawable in drawable_grp:
            drawable.draw(screen)
    
        pygame.display.flip()


if __name__ == "__main__":
    main()

