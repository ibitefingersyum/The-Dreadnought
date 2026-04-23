import pygame
import random
from enemy_data import ENEMY_TYPES


class Enemy:
    def __init__(self, enemy_type, x, y):
        self.type = enemy_type
        self.data = ENEMY_TYPES[enemy_type]

        self.pos = pygame.Vector2(x, y)
        self.speed = 100

        self.ability = self.data.get("ability", None)
        self.weapon = self.data.get("weapon", None)

    def update(self, dt, player):
        direction = player.pos - self.pos

        if direction.length() > 0:
            direction = direction.normalize()

        self.pos += direction * self.speed * dt

        self.use_ability(dt, player)

    def use_ability(self, dt, player):
        if self.ability == "heal_allies":
            pass
        elif self.ability == "buff_allies":
            pass
        elif self.ability == "place_traps":
            pass
        elif self.ability == "build_cover":

            pass

        

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 60, 60), self.pos, 15)


class EnemyManager:
    def __init__(self):
        self.enemies = []

        self.spawn_enemy(200, 200) #temporary enemies, will make spawning once base game is finished.
        self.spawn_enemy(500, 200) #temporary enemies, will make spawning once base game is finished.

    def pick_enemy_type(self):
        pool = []
        for name, data in ENEMY_TYPES.items():
            pool += [name] * data["weight"]
        return random.choice(pool)

    def spawn_enemy(self, x, y):
        enemy_type = self.pick_enemy_type()
        enemy = Enemy(enemy_type, x, y)
        self.enemies.append(enemy)

    def update(self, dt, player):
        for e in self.enemies:
            e.update(dt, player)

    def draw(self, screen):
        for e in self.enemies:
            e.draw(screen)

            