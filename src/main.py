import pygame
from player import Player
from enemies import EnemyManager
from projectiles import ProjectileManager
from vision import draw_vision_cone
from map import draw_map
from hud import draw_hud #add stuff from other files
pygame.display.set_caption("The Dreadnought") #cool launch name thing

pygame.init()
WIDTH, HEIGHT = 600, 800  #map size adjust later
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player(WIDTH//2, HEIGHT-100)
enemies = EnemyManager()
projectiles = ProjectileManager()

running = True
while running:
    dt = clock.tick(60) / 1000 #frame rate time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # updates
    player.update(dt)
    enemies.update(dt, player)
    projectiles.update(dt)

    # everything draw related
    screen.fill((10, 10, 30))
    draw_map(screen)

    draw_vision_cone(screen, player.pos, player.angle)

    player.draw(screen)
    enemies.draw(screen)
    projectiles.draw(screen)

    draw_hud(screen, player)

    pygame.display.flip()

    #plans: add pausing upon menu open, force game stop end end screen when player dies.

pygame.quit()

#ngl ai generated like a solid 60-70% of this