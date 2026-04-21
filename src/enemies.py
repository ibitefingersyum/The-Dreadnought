#enemies

import pygame

class Enemy:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)

    def update(self, dt, player):
        pass  # add AI later

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 50, 50), self.pos, 15)


class EnemyManager:
    def __init__(self):
        self.enemies = [Enemy(200, 200), Enemy(600, 200)]

    def update(self, dt, player):
        for e in self.enemies:
            e.update(dt, player)

    def draw(self, screen):
        for e in self.enemies:
            e.draw(screen)

# type of enemy

# Soldat (Increased ) 3 Weight
# Rook (Creates buildings) 2 Weight
# Mortician (Minor Buffs, Heals other enemies) 2 Weight
# Officer (Buffs other enemies) 2 Weight
# Jaeger (Traps) 2 Weight
# Lancer (Charges) 1 Weight | Heavy Lance forced | (No Survivalist interaction for simplicity)
# Vanguard (Shield) 2 Weight | Shield forced |

# Shock Troopers (Elites) Forced respective weapons (Set Perks)


# Enemy perk
#Survivalist (+1 Weight), unique class interactions. (+1 Buff Officer, +Ability use-rate for: Rook, Mortician, Jaeger)

#Enemy Weapons
    # 2 Weight:
        # Judgement (High Damage, Mid Accuracy, -Low RoF) (rifle) | 1 bullet | 3s reload | 200 dmg | 21 rpm
        # Prince (+Mid Damage, High Accuracy, Mid RoF) (rifle) | 7 bullets | 4s reload | 150 dmg | 60 rpm
        # Jesse (Mid Damage, -Mid Accuracy, Mid+ RoF) (rifle) | 10 bullets | 5.5s reload | 130 dmg | 75 rpm
        # Hellion (High Damage, -Low Accuracy, High RoF) (shotgun) |6 bullets | 7.75s reload | 22x9 dmg| 150 rpm

    # 1 Weight:
        # Grace Mid Damage, +Mid Accuracy, +Mid RoF (Revolver) | 6 Bullets | 4.75s reload | 120 dmg | 80 rpm
        # Insurgent Low Damage, -Low Accuracy, ++High RoF (Handgun) | 20 Bullets | Can't Reload | 60 dmg | 230 rpm

    # Special (1w): (Heavy Lance, Shield )
        # Heavy Lance | Special logic, make lancer zoom in a straight line, dealing 300 damage on hit
        # Shield | Special logic, set down shield that can be destroyed

