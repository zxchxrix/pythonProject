
def find_emoji(input):
    sentenceSplit = input.split()
    emojis = {':)': '😊',
              '):': '☹️',
              'XD': '😆'}
    output = ''
    for word in sentenceSplit:
        output += emojis.get(word, word) + ' '
    return output

inputString = input('> ')
print(find_emoji(inputString))