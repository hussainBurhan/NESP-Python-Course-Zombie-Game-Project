# Import the 'random' module for generating random numbers
import random

# Define a class named 'Enemy' to represent an enemy in the game
class Enemy():
    # Constructor method to initialize enemy attributes
    def __init__(self, name='Enemy', hit_point=0, lives=1):
        self.name = name
        self.hit_points = hit_point
        self.lives = True
    
    # Method to simulate enemy taking damage
    def take_damage(self, damage):
        remaining_point = self.hit_points - damage
        if remaining_point >= 0:
            self.hit_points = remaining_point
            print(f'I took a bullet and took {damage} point damage, my remaining life is {remaining_point}')
        else:
            self.lives -= 1
            if self.lives > 0:
                print(f'{self.name} lost life')
            else:
                print(f'Aaaarrrrgggghhhh, {self.name} died')
                self.lives = False
    
    # String representation of the Enemy object
    def __str__(self):
        return f'Enemy : {self.name}, Enemy lives : {self.lives}, Hit points : {self.hit_points}'

# Define a subclass 'Bone_snatcher' inheriting from 'Enemy'
class Bone_snatcher(Enemy):
    # Constructor for Bone_snatcher with custom values
    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_point=23)
    
    # Custom method for Bone_snatcher
    def snatch(self):
        return f'I am {self.name}, I just snatched your weapon'

# Define a subclass 'Blood_drinker' inheriting from 'Enemy'
class Blood_drinker(Enemy):
    # Constructor for Blood_drinker with custom values
    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_point=50)
    
    # Custom method for Blood_drinker to dodge attacks
    def duck(self):
        if random.randint(1, 5) == 5:
            print(f'{self.name} ducked your attack')
            return True
        else:
            return False
    
    # Override the take_damage method to incorporate dodging
    def take_damage(self, damage):
        if not self.duck():
            super().take_damage(damage=damage)

# Define a subclass 'KingBloodDrinker' inheriting from 'Blood_drinker'
class KingBloodDrinker(Blood_drinker):
    # Constructor for KingBloodDrinker with modified hit points
    def __init__(self, name):
        super().__init__(name)
        self.hit_points = 150
    
    # Override the take_damage method to reduce damage further
    def take_damage(self, damage):
        super().take_damage(damage//4)
