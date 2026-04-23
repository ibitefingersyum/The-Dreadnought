import pygame
import math

def draw_vision_cone(surface, pos, angle):
    length = 1200
    spread = math.radians(30)

    left = angle - spread
    right = angle + spread

    p1 = pos
    p2 = pos + pygame.Vector2(math.cos(left), math.sin(left)) * length
    p3 = pos + pygame.Vector2(math.cos(right), math.sin(right)) * length

    pygame.draw.polygon(surface, (200, 200, 200), [p1, p2, p3])

#attempt at making a small vision circle around the player

# def draw_vision_circle(surface, pos, radius):
