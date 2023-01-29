def greet_user(firstName, lastName):   # passing parameters
    print(f'Hi {firstName} {lastName}!')
    print('Welcome aboard')


print('Start')
greet_user('Zac', 'Salad')   # passing arguments, positional arguments
greet_user(lastName='Jude', firstName='Alexa')  # keyword arguments
print('Finish')

print('\n---\n')


def square(number):
    return number * number

print(square(4))

