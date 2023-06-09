class Weapon:
    def __init__(self, name: str, base_damage: int, defense: int, hit_chance: int, affinity: str):
        self.name = name
        self.base_damage = base_damage
        self.defense = defense
        self.hit_chance = hit_chance
        self.affinity = affinity

class Sword(Weapon):
    def __init__(self, name: str, base_damage: int, defense: int, hit_chance: int, affinity: str, warcry_duration: int, poison_duration: int, whirlwind_duration: int):
        super().__init__(name, base_damage, defense, hit_chance, affinity)
        self.warcry_duration = warcry_duration
        self.poison_duration = poison_duration
        self.whirlwind_duration = whirlwind_duration

    def start_of_turn(self):
        self.whirlwind_duration -= 1
        self.warcry_duration -= 1
        self.poison_duration -= 1


    def whirlwind(self):
        self.whirlwind_duration += 2

    def decapitate(self, enemy):
        damage = self.base_damage * (1 + (1 - enemy.currenthealt/enemy.maxhealth))
        enemy.take_damage(self, damage)

        if self.poison_duration > 0:
            enemy.poison()

    


class Bow(Weapon):
    def __init__(self, name: str, base_damage: int, defense: int, hit_chance: int, affinity: str, burning_duration: int):
        super().__init__(name, base_damage, defense, hit_chance, affinity)
        self.burning_duration = burning_duration

class Wand(Weapon):
    def __init__(self, name: str, damage: int, defense: int, hit_chance: int, affinity: str, shield_duration: int):
        super().__init__(name, damage, defense, hit_chance, affinity)
        self.shield_duration = shield_duration
