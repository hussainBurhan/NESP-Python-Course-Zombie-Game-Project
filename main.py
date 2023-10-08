# Import classes from player and enemy modules
from player import Player
from enemy import Enemy, Bone_snatcher, Blood_drinker, KingBloodDrinker
import random

# Create an instance of the Player class for 'Hussain' with an initial balance of 50 dollars
Hussain = Player("Hussain")
print(Hussain)

# Create instances of different enemy types
Bone_Snatcher = Bone_snatcher("Bone Snatcher")
print(Bone_Snatcher)

Vampire = Blood_drinker("Vampire")
print(Vampire)

Dracula = KingBloodDrinker("Dracula")
print(Dracula)

# Simulate combat scenarios with enemies
while Bone_Snatcher.lives:
    Bone_Snatcher.take_damage(random.randint(1, 10))

print('x'*40)

while Vampire.lives:
    Vampire.take_damage(random.randint(1, 10))

print('x'*40)

while Dracula.lives:
    Dracula.take_damage(random.randint(1, 10))
