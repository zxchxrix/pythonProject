# def max_num():
#     numbers = []
#     numInput = input('Enter a number for the list> ')
#     while numInput != 'q':
#         numbers.append(numInput)
#         numInput = input('Enter a number for the list> ')
#     max = numbers[0]
#     for num in numbers:
#         if num > max:
#             max = num
#     print(f'Your largest number is {num}')

def find_max(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max

