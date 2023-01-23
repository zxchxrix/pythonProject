names = ['Messi', 'LeBron', 'Cristiano', 'Bukayo', 'Mesut']
print(names[:3])

numbers = [7, 18, 4, 22, 3, 1, 67]
maxNum = numbers[0]

for num in numbers:
    if num > maxNum:
        maxNum = num
    print(f'{num}, {maxNum}')