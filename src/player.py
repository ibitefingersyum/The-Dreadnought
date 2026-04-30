import pygame
import math
import random
from health import Health

class Projectile:
    def __init__(self, x, y, angle, speed=400):
        self.pos = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(math.cos(angle), math.sin(angle)) * speed
        self.radius = 5
        self.lifetime = 5.0
        self.age = 0

    def update(self, dt):
        self.pos += self.velocity * dt
        self.age += dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), self.pos, self.radius)

    def is_alive(self):
        return self.age < self.lifetime

class Player:
    def __init__(self, x, y): 
        self.pos = pygame.Vector2(x, y)
        self.speed = 60 # movement speed
        self.angle = 0
        self.radius = 20
        self.vision_range = 300
        self.vision_angle = math.pi / 3
        self.health = Health(11000, drain_rate=18)  #health drain and initial hp
        self.projectiles = []
        self.shoot_cooldown = 0.1
        self.shoot_timer = 0
        self.spread_angle = math.pi / 12  # 15 degree spread
        self.survival_time = 0

    def get_rect(self):
        return pygame.Rect(self.pos.x - self.radius, self.pos.y - self.radius, self.radius * 2, self.radius * 2)

    def is_in_vision(self, target_pos):
        """Check if target is within player's vision cone"""
        direction_to_target = target_pos - self.pos
        distance = direction_to_target.length()
        
        if distance > self.vision_range:
            return False
        
        if distance == 0:
            return True
        
        angle_to_target = math.atan2(direction_to_target.y, direction_to_target.x)
        angle_diff = abs(angle_to_target - self.angle)
        
        while angle_diff > math.pi:
            angle_diff -= 2 * math.pi
        
        return abs(angle_diff) <= self.vision_angle / 2

    def check_wall_collision(self, screen_width, screen_height):
        if self.pos.x - self.radius < 0:
            self.pos.x = self.radius
        elif self.pos.x + self.radius > screen_width:
            self.pos.x = screen_width - self.radius
        
        if self.pos.y - self.radius < 0:
            self.pos.y = self.radius
        elif self.pos.y + self.radius > screen_height:
            self.pos.y = screen_height - self.radius

    def update(self, dt, screen_width=None, screen_height=None, enemies=None):
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

        # Shooting with spread
        self.shoot_timer -= dt
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0] and self.shoot_timer <= 0:
            spread = random.uniform(-self.spread_angle / 2, self.spread_angle / 2)
            self.projectiles.append(Projectile(self.pos.x, self.pos.y, self.angle + spread))
            self.shoot_timer = self.shoot_cooldown

        # Update projectiles
        for projectile in self.projectiles[:]:
            projectile.update(dt)
            if not projectile.is_alive():
                self.projectiles.remove(projectile)

        if screen_width and screen_height:
            self.check_wall_collision(screen_width, screen_height)

        self.health.update(dt)
        
        # Increase survival time
        self.survival_time += dt

    def draw(self, screen):
        pygame.draw.circle(screen, (150, 0, 200), self.pos, self.radius)
        for projectile in self.projectiles:
            projectile.draw(screen)