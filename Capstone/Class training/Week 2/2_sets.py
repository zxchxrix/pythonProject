# unordered list
# no duplicates

cats = set()        # create empty set
cats.add('Lion')
cats.add('Tiger')
cats.add('Leopard')
print(cats)
cats.add('Cheetah')
print(cats)

birds = {'owl', 'robin', 'swan'}
print(birds)
birds.add('owl')
print(birds)
birds.remove('swan')
print(birds)

birdList = ['eagle', 'toucan', 'chicken', 'falcon', 'swan', 'eagle', 'swan']
noDupeBirdList = set(birdList)
print(noDupeBirdList)

