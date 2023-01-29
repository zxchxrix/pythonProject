# The classes a student is registered for
classes_registered = ['ITEC 1150', 'ITEC 1100', 'ENG 1340', 'MATH 1100']

# Make a list of only the ITEC classes
only_itec = [ c for c in classes_registered if c.startswith('ITEC')]
print(only_itec)

itec_Classes = []
for clas in classes_registered:
    if clas.startswith('ITEC'):
        itec_Classes.append(clas)

for clas in itec_Classes:
    print(clas)

# Record temperature every day. Record -1 if not possible to take measurement.
high_temps = [-1, 78, 72, 67, -1, 51, 87, 82, -1, 54, 67, 78, -1, 70]

# make a list of only numbers that represent a valid temperature measurement
only_valid = [ v for v in high_temps if v > 0 ]
print(only_valid)

# make a list that adds 1 to each value
numbers = [2, 4, 6]
added_one = [ n + 1 for n in numbers ]
print(added_one)

# filtering non-zero nummbers
numbersList = [ 8, 0, 43, 11, 2, 0, 55, 6]
non_zeros = [ n for n in numbersList if n != 0 ]
print(non_zeros)
non_zeros_doubled = [ n * 2 for n in numbersList if n != 0 ]
print(non_zeros_doubled)