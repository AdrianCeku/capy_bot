import random

from character import Character
from weapon import Melee


class Orc(Character):
    def __init__(self, name: str, level: int, maxhp: int, power: int, armor: int, stamina: str, element: str,
                 weapon: Melee):
        super().__init__(name, level, maxhp, power, armor, element, weapon)
        self.stamina = stamina

    def barricade(self):
        pass


class Viking(Character):
    def __init__(self, name: str, level: int, maxhp: int, power: int, armor: int, element: str,
                 weapon: Melee):
        super().__init__(name, level, maxhp, power, armor, element, weapon)
        self.stamina = 100

    def berserk(self):
        bonus_damage = (self.level + self.power) / 10
        self.power += bonus_damage
        print(f'{self.name} enrages, his attack power increases by {bonus_damage}')

    def take_damage(self, damage):
        super().take_damage(damage)
        if self.hp <= self.maxhp / 3:
            self.berserk()




