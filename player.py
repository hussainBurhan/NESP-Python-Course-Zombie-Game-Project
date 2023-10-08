# Define a class named 'Player' to represent a player in the game
class Player():
    # Constructor method to initialize player attributes
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self.score = 0
    
    # Getter method for retrieving lives
    def _get_lives(self):
        return self._lives
    
    # Setter method for setting lives (with validation)
    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print('Lives cannot be less than zero')
            self._lives = 0
    
    # Getter method for retrieving level
    def _get_level(self):
        return self._level
    
    # Setter method for setting level (with score update)
    def _set_level(self, level):
        if level >= 0:
            delta = level - self._level
            self.score += (delta * 100)
            self._level = level
        else:
            print('Lives cannot be less than zero')
    
    # Define 'lives' property using the defined getters and setters
    lives = property(_get_lives, _set_lives)
    level = property(_get_lives, _set_level)
    
    # String representation of the Player object
    def __str__(self):
        return f'Name : {self.name}, Lives : {self.lives}, Level : {self.level}, Score : {self.score}'
