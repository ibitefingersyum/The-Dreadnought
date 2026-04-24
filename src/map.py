import pygame

def draw_map(screen):
    # simple placeholder clouds
    for i in range(5):
        pygame.draw.circle(screen, (50, 50, 50), (150*i+50, 300), 40)

#yay