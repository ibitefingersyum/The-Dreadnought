import pygame
import math
from health import Health

class Player:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.speed = 50
        self.angle = 0
        self.health = Health(12000, drain_rate=20)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.pos.y -= self.speed * dt
        if keys[pygame.K_s]:
            self.pos.y += self.speed * dt
        if keys[pygame.K_a]:
            self.pos.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.pos.x += self.speed * dt

        mouse = pygame.mouse.get_pos()
        direction = pygame.Vector2(mouse) - self.pos
        self.angle = math.atan2(direction.y, direction.x)

        self.health.update(dt)

    def draw(self, screen):
        pygame.draw.circle(screen, (150, 0, 200), self.pos, 20)