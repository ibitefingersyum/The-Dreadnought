import pygame

def draw_hud(screen, player):
    font = pygame.font.Font(None, 36)
    
    # Display health
    health_text = font.render(f"Health: {int(player.health.current)}/{int(player.health.max)}", True, (255, 0, 0))
    screen.blit(health_text, (10, 10))
    
    # Display survival time
    time_text = font.render(f"Time: {int(player.survival_time)}s", True, (100, 255, 100))
    screen.blit(time_text, (10, 50))