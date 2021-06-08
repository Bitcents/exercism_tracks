from random import randint

class Character:
    def __init__(self):
        self.strength = None
        self.intelligence = None
        self.dexterity = None
        self.constitution = None
        self.wisdom = None
        self.charisma = None
        self.__generate_stats()
        self.hitpoints = 10 + modifier(self.constitution)

    def __generate_stats(self):
        self.strength = score()
        self.intelligence = score()
        self.dexterity =  score() 
        self.constitution = score() 
        self.wisdom =  score() 
        self.charisma =  score()

    def ability(self):
        return self.strength
   
def score():
    min_number = 7 # dice rolls cannot be larger than 6
    dice_rolls = []
    for _ in range(3):
        roll = randint(1,6)
        if roll < min_number:
            min_number = roll
        dice_rolls.append(roll)
    return sum(dice_rolls) - min_number

def modifier(constitution):
    modifier = (constitution - 10)//2
    return modifier 
