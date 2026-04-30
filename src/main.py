import pygame
from player import Player
from enemies import EnemyManager
from vision import draw_vision_cone
from map import draw_map
from hud import draw_hud
from start_screen import StartScreen

pygame.display.set_caption("The Dreadnought")

pygame.init()
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Start screen
start_screen = StartScreen(WIDTH, HEIGHT)
running = True
while running and not start_screen.is_done():
    running = start_screen.handle_events()
    start_screen.draw(screen)

if not running:
    pygame.quit()
    exit()

player = Player(WIDTH//2, HEIGHT-100)
enemies = EnemyManager(WIDTH, HEIGHT)

paused = True
font = pygame.font.Font(None, 40)

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    if not paused:
        player.update(dt, WIDTH, HEIGHT, enemies.enemies)
        enemies.update(dt, player)

    screen.fill((10, 10, 30))
    draw_map(screen)

    draw_vision_cone(screen, player.pos, player.angle)

    player.draw(screen)
    enemies.draw(screen, player)

    draw_hud(screen, player)

    if paused:
        pause_text = font.render("PAUSED - Press SPACE to Resume", True, (255, 255, 0))
        pause_rect = pause_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        pygame.draw.rect(screen, (0, 0, 0), pause_rect.inflate(20, 20))
        screen.blit(pause_text, pause_rect)

    pygame.display.flip()

pygame.quit()

#ngl ai generated like a solid 60-70% of this