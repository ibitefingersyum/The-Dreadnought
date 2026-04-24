import pygame

class Projectile:
    def __init__(self, pos, vel):
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(vel)

    def update(self, dt):
        self.pos += self.vel * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), self.pos, 5)

#completely unused btw
class ProjectileManager:
    def __init__(self):
        self.projectiles = []

    def update(self, dt):
        for p in self.projectiles:
            p.update(dt)

    def draw(self, screen):
        for p in self.projectiles:
            p.draw(screen)