import pygame
import random
import math
from enemy_data import ENEMY_TYPES


class Projectile:
    def __init__(self, x, y, angle, speed=300, is_elite=False):
        self.pos = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(math.cos(angle), math.sin(angle)) * speed
        self.radius = 4
        self.lifetime = 8.0
        self.age = 0
        self.is_elite = is_elite

    def update(self, dt):
        self.pos += self.velocity * dt
        self.age += dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 100, 100), self.pos, self.radius)

    def is_alive(self):
        return self.age < self.lifetime


class Enemy:
    def __init__(self, enemy_type, x, y):
        self.type = enemy_type
        self.data = ENEMY_TYPES[enemy_type]

        self.pos = pygame.Vector2(x, y)
        self.speed = 100
        self.radius = 15
        self.stopping_distance = 200
        self.health = self.data.get("health", 200)
        self.max_health = self.health
        self.ability = self.data.get("ability", None)
        self.weapon = self.data.get("weapon", None)
        self.projectiles = []
        self.shoot_cooldown = 1
        self.shoot_timer = 0
        self.spread_angle = math.pi / 18  # 10 degree spread

    def get_rect(self):
        return pygame.Rect(self.pos.x - self.radius, self.pos.y - self.radius, self.radius * 2, self.radius * 2)

    def take_damage(self, amount):
        self.health -= amount
        return self.health <= 0

    def is_alive(self):
        return self.health > 0

    def update(self, dt, player, enemies):
        direction = player.pos - self.pos
        distance = direction.length()

        if distance > self.stopping_distance and distance > 0:
            direction = direction.normalize()
            self.pos += direction * self.speed * dt
        
        # Enemy-to-enemy collision avoidance
        for other in enemies:
            if other is not self:
                other_dir = other.pos - self.pos
                other_distance = other_dir.length()
                if other_distance < self.radius + other.radius and other_distance > 0:
                    collision_dir = (self.pos - other.pos).normalize()
                    self.pos += collision_dir * self.speed * dt * 0.5

        # Shoot when within stopping distance
        if distance <= self.stopping_distance and distance > 0:
            angle = math.atan2(direction.y, direction.x)
            self.shoot(angle)

        self.shoot_timer -= dt
        for projectile in self.projectiles[:]:
            projectile.update(dt)
            if not projectile.is_alive():
                self.projectiles.remove(projectile)

        self.use_ability(dt, player)

    def shoot(self, angle):
        if self.shoot_timer <= 0:
            spread = random.uniform(-self.spread_angle / 2, self.spread_angle / 2)
            self.projectiles.append(Projectile(self.pos.x, self.pos.y, angle + spread, is_elite=False))
            self.shoot_timer = self.shoot_cooldown

    def use_ability(self, dt, player): #unused for now
        if self.ability == "heal_allies":
            pass
        elif self.ability == "buff_allies":
            pass
        elif self.ability == "place_traps":
            pass
        elif self.ability == "build_cover":

            pass

        

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 60, 60), self.pos, self.radius)
        for projectile in self.projectiles:
            projectile.draw(screen)


class EliteEnemy(Enemy):
    def __init__(self, x, y):
        self.type = "elite"
        self.data = {}
        self.pos = pygame.Vector2(x, y)
        self.speed = 100
        self.radius = 18
        self.stopping_distance = 200
        self.health = 300
        self.max_health = 300
        self.ability = None
        self.weapon = None
        self.projectiles = []
        self.shoot_cooldown = 0.1
        self.shoot_timer = 0
        self.spread_angle = math.pi / 12

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), self.pos, self.radius)
        for projectile in self.projectiles:
            projectile.draw(screen)


class EnemyManager:
    def __init__(self, screen_width=800, screen_height=600):
        self.enemies = []
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.spawn_margin = 50
        self.spawn_timer = 0
        self.spawn_interval = 0.75

        self.spawn_enemy_random()
        self.spawn_enemy_random()

    def pick_enemy_type(self):
        pool = []
        for name, data in ENEMY_TYPES.items():
            pool += [name] * data["weight"]
        return random.choice(pool)

    def spawn_enemy(self, x, y):
        enemy_type = self.pick_enemy_type()
        enemy = Enemy(enemy_type, x, y)
        self.enemies.append(enemy)

    def spawn_enemy_random(self):
        x = random.randint(self.spawn_margin, self.screen_width - self.spawn_margin)
        y = random.randint(self.spawn_margin, self.screen_height - self.spawn_margin)
        
        # 1/75 chance to spawn elite enemy
        if random.randint(1, 75) == 1:
            self.enemies.append(EliteEnemy(x, y))
        else:
            self.spawn_enemy(x, y)

    def update(self, dt, player):
        # Spawn new enemies
        self.spawn_timer -= dt
        if self.spawn_timer <= 0:
            self.spawn_enemy_random()
            self.spawn_timer = self.spawn_interval

        for e in self.enemies[:]:
            # Only update visible enemies
            if player.is_in_vision(e.pos):
                e.update(dt, player, self.enemies)
        
        # Remove dead enemies
        self.enemies = [e for e in self.enemies if e.is_alive()]
        
        # Check collision with player projectiles
        for e in self.enemies:
            for projectile in player.projectiles[:]:
                if e.get_rect().collidepoint(projectile.pos):
                    if e.take_damage(130):
                        pass
                    player.projectiles.remove(projectile)
                    break

        # Check collision with enemy projectiles hitting player
        for e in self.enemies:
            for projectile in e.projectiles[:]:
                if player.get_rect().collidepoint(projectile.pos):
                    damage = 100 if projectile.is_elite else 100
                    player.health.current -= damage
                    e.projectiles.remove(projectile)
                    break

    def draw(self, screen, player):
        for e in self.enemies:
            # Only draw visible enemies
            if player.is_in_vision(e.pos):
                e.draw(screen)

