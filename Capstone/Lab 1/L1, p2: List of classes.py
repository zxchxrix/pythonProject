classes = []
classNum = 1

print('Type in the classes you are taking this year. Write \'quit\' to complete list.')
userTaking = input(f'Class {classNum}> ')
while userTaking != 'quit':
    classes.append(userTaking)
    classNum += 1
    userTaking = input(f'Class {classNum}> ')


print('Here are the list of your class:')
for clas in classes:
    print('\t-' + clas)

