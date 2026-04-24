class Health:
    def __init__(self, max_health, drain_rate=0):
        self.max = max_health
        self.current = max_health
        self.drain_rate = drain_rate

    def update(self, dt): #drain stolen to player
        self.current -= self.drain_rate * dt
        if self.current < 0:
            self.current = 0

    def take_damage(self, amount): #after i figure out projectiles
        self.current -= amount
        if self.current < 0:
            self.current = 0

    def is_dead(self):
        return self.current <= 0
    
    # temp until needed