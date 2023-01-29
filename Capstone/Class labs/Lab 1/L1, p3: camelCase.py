sentence = input('Input words to camelCase: ')
camelCased = ''
splitSentence = sentence.split()
for word in splitSentence:
    camelCased += word.capitalize()
print('> ' + camelCased[0].lower() + camelCased[1:])

print('in banner now!')