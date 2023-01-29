# immutable list (tuple) of animals
animals = ('lion', 'puma', 'tiger')

try:
# unpacking the tuple using variables assigned to animals in the list.
    lion, tiger = animals
except:
    print('Oops, that does not exist.')

# since tiger is the third variable, it was assigned animals[2]
# print(tiger)