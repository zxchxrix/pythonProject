message = input('> ')

emojis = {
    ':)': '😊',
    ':(': '☹️'
}

output = ''
for word in message.split(' '):
    if word in emojis:
        output += emojis.get(word, word) + ' '
    else:
        output += word + ' '

print(output)