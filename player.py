import time
class player:
    def __init__(self, name, health,alive):
        self.name = name
        self.health = health
        self.alive = alive
    
class enemie:
    def __init__(self, damage,health,alive):
        self.damage = damage
        self.health = health
        self.alive = alive
    