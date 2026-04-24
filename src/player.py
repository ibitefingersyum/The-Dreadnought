import pygame
import math
from health import Health

class Player:
    def __init__(self, x, y): 
        self.pos = pygame.Vector2(x, y)
        self.speed = 60 # movement speed
        self.angle = 0
        self.health = Health(11000, drain_rate=18)  #health drain and initial hp

    def update(self, dt):
        keys = pygame.key.get_pressed()
#WASD movement (ai generated I have no idea how to make this)
        if keys[pygame.K_w]:
            self.pos.y -= self.speed * dt
        if keys[pygame.K_s]:
            self.pos.y += self.speed * dt
        if keys[pygame.K_a]:
            self.pos.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.pos.x += self.speed * dt
#look at cursor (also ai generated cause how does one make this)
        mouse = pygame.mouse.get_pos()
        direction = pygame.Vector2(mouse) - self.pos
        self.angle = math.atan2(direction.y, direction.x)

        self.health.update(dt)

    def draw(self, screen):
        pygame.draw.circle(screen, (150, 0, 200), self.pos, 20)