import random

from character import Magician
from config import names, affinities
from enemy import Viking
from weapon import Magic, Melee


# generates enemy based on player stats
def generate_enemy(player):
    name = random.choice(names['vikings'])
    level = player.level + random.randint(-5, 5)
    maxhp = player.maxhp + random.randint(-100, 100)
    power = player.power + random.randint(-10, 10)
    armor = player.armor + random.randint(-30, 30)
    element = 'None'
    weapon = Melee(f'Axe of {random.choice(affinities)}', 10)
    return Viking(name, level, maxhp, power, armor, element, weapon)


def initiate_battle():
    player = Magician('Jens Bieleit', 100, 690, 30, 10, 'Grass', Magic('Joint', 80))
    enemy = generate_enemy(player)

    while player.is_alive and enemy.is_alive:
        player.attack(enemy)
        enemy.attack(player)

    if player.is_alive:
        print(f'{player.name} wins')
    elif enemy.is_alive:
        print(f'{enemy.name} wins')


if __name__ == "__main__":
    initiate_battle()
