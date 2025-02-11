import pygame
from constants import * 
from player import Player
from asteroid import Asteroid

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    asteroid_grp = pygame.sprite.Group()
    updatable_grp = pygame.sprite.Group()
    drawable_grp = pygame.sprite.Group()
    Player.containers = (updatable_grp, drawable_grp)
    Asteroid.containers = (asteroid_grp, updatable_grp, drawable_grp)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000
        pygame.Surface.fill(screen, (0,0,0))
        for drawable in drawable_grp:
            drawable.draw(screen)
        updatable_grp.update(dt)
        pygame.display.flip()



if __name__ == "__main__":
    main()

