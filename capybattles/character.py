from weapon import Weapon, Ranged, Magic
from config import affinities


class Character:
    def __init__(self, name: str, level: int, maxhp: int, power: int, armor: int, element: str, weapon: Weapon):
        self.name = name
        self.level = level
        self.maxhp = maxhp
        self.hp = maxhp
        self.power = power
        self.element = element
        self.armor = armor
        self.weapon = weapon
        self.is_alive = True

    def knock_out(self):
        self.is_alive = False

    def take_damage(self, weapon, damage):
        self.hp -= damage - self.armor
        print(f'{self.name} takes {damage} damage')
        if self.hp <= 0:
            self.knock_out()
            print(f'{self.name} was defeated')
        if weapon.affinity == "Fire":
            self.burning()

    def attack(self, target):
        damage = self.power + self.weapon.base_damage
        print(f'{self.name} attacks {target.name} with {self.weapon.name}')
        target.take_damage(damage)


class Warrior(Character):
    def __init__(self, name: str, level: int, maxhp: int, power: int, armor: int, element: str, weapon: Magic):
        super().__init__(name, level, maxhp, power, armor, element, weapon)


class Ranger(Character):
    def __init__(self, name: str, level: int, maxhp: int, power: int, armor: int, element: str, weapon: Ranged):
        super().__init__(name, level, maxhp, power, armor, element, weapon)


class Magician(Character):
    def __init__(self, name: str, level: int, maxhp: int, power: int, armor: int, element: str, weapon: Magic):
        super().__init__(name, level, maxhp, power, armor, element, weapon)
