import random


# for i in range(3):
#     print(random.random())
#     print('---')
#     print(random.randint(10, 50))
#
# # returning random item from list
# members = ['Alex', 'Bukayo', 'Kart', 'Borat']
# leader = random.choice(members)
# print(leader)

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
