# using int
temp = 62

if temp >= 69:
    print('It is a hot day. Drink plenty of water.')
elif temp <= 55:
    print('Yikes! it\'s a little chilly out. Wear some warm clothes.')
else:
    print('Its a lovely day, init.')

# using boolean
is_hot = False
is_cold = True

if is_hot:
    print('It is a hot day. Drink plenty of water.')
elif is_cold:
    print('Yikes! it\'s a little chilly out. Wear some warm clothes.')
else:
    print('Its a lovely day, init.')

# home buying exercize
housePrice = 1000000
goodCredit = True

if goodCredit:
    print(f'Your down payment is 10%: ${housePrice * .1}')
else:
    print(f'Because you do not have good credit, your down payment is 20%: ${housePrice * .2}')
