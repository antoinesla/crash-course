from random import randint
import time

class Dice:
    '''tutorial class to model dice with user-defined number of sides'''

    def __init__(self, sides):
        '''initializes dice with number of sides'''
        self.sides = sides

    def roll_dice(self):
        '''return random number up to number of sides the dice has'''
        return randint(1,self.sides)

d6 = Dice(6)
d10 = Dice(10)

while True:
    print(d6.roll_dice() + d10.roll_dice())
    time.sleep(0.25)

