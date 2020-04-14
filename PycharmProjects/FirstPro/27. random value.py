#Python Module Index
#https://docs.python.org/3/py-modindex.html

import random

for i in range(3):
    #print(random.random())
    print(random.randint(10,100))


#random choice leader

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)


#simple program
class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second


dice = Dice()
print(dice.roll())