import pygame
from player import Player
from enemies import EnemyManager
from projectiles import ProjectileManager
from vision import draw_vision_cone
from map import draw_map
from hud import draw_hud

pygame.init()
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player(WIDTH//2, HEIGHT-100)
enemies = EnemyManager()
projectiles = ProjectileManager()

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # UPDATE
    player.update(dt)
    enemies.update(dt, player)
    projectiles.update(dt)

    # DRAW
    screen.fill((0, 0, 0))
    draw_map(screen)

    draw_vision_cone(screen, player.pos, player.angle)

    player.draw(screen)
    enemies.draw(screen)
    projectiles.draw(screen)

    draw_hud(screen, player)

    pygame.display.flip()

pygame.quit()