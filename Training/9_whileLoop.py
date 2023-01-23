# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1
# print('done')

# name1 = 'Jibril'
# name2 = 'Patrick'
#
# print(f'{name1} and {name2} are friends')
# print(f'{name1} and {name2} are friends')
# print(f'{name1} and {name2} are friends')

secretNum = 7
attempt = 1

while attempt <= 3:
    guess = int(input(f'Guess {attempt}: '))
    if guess == secretNum:
        print(f'You got it! The secret number is: {guess}')
        break
    else:
        print(f'Sorry. {guess} is not the secret number. Try again!')
        attempt += 1

if attempt == 4:
    print(f'Sorry you are all out of attempts. The secret number was {secretNum}')
else:
    print('Great job on getting the secret number. Try the game again!')

