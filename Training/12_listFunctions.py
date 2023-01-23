numbers = [5, 8, 1, 2, 8, 8, 10, 4, 4, 1, 8]

# append a number
numbers.append(13)
print(numbers)

# insert a number into an index
numbers.insert(1, 99)
print(numbers)

# remove a number
numbers.remove(13)
print(numbers)

# remove all numbers in the list
# numbers.clear()

# remove last item in a list
numbers.pop()
print(numbers)

# find index of an item in the list
print(numbers.index(8))

# check for the existence of a value
print(50 in numbers)

# check the number of occurences of a value
print(numbers.count(8))

# sort list
numbers.sort()
print(numbers)
# sort in reverse
numbers.reverse()
print(numbers)

# My way using while loop nested in a for loop
for num in numbers:
    occ = numbers.count(num)
    while occ > 1:
        numbers.remove(num)
        occ = numbers.count(num)
print(numbers)

# Mosh's way was using two lists - makes sense

