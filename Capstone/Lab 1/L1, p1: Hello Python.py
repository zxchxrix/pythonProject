name = input('Hello, what is your name? ')
print(f'Hello {name}. You have {len(name)} letters in your name :)')

currentMonth = 'January'
monthBorn = input(f'\nWhat month were you born, {name}? ')
if monthBorn == currentMonth:
    print('Ayyy! Happy birthday month!')
else:
    print('Well, it\'s not your birthday month, but it is your birthday year')