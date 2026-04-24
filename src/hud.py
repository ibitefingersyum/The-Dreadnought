import pygame

def draw_hud(screen, player):
    font = pygame.font.SysFont(None, 30)
    text = font.render(f"Health: {int(player.health.current)}", True, (255,255,255))
    screen.blit(text, (10, 10))

    #currently just health