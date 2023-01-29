# list of tuples
cityState = [('Minneapolis', 'MN'), ('New York City', 'NY'), ('Chicago', 'IL'), ('Houston', 'TX'), ('Saint Paul', 'MN')]

# 5 items contained in the list
print(len(cityState))

# indexing an items (tuple) in the list
firstCityState = cityState[0]
print(firstCityState)
print(firstCityState[0])
print(firstCityState[1])

# unpacking
# can write more than one variable, separated by a comma (,) and assign them values in the list in order
city, state = firstCityState
print(city, state)

# immutable list (tuple) of animals
animals = ('lion', 'puma', 'tiger')

# unpacking the tuple using variables assigned to animals in the list.
lion, puma, tiger = animals

# since tiger is the third variable, it was assigned animals[2]
print(tiger)


# variable amounts must match tuple length

# ------

# other uses for tuples
def getDistance():
    miles = 1000
    km = miles * 1.6
    return miles, km

# getDistance returns miles, km
distances = getDistance()
print(distances)

# index the second item returned
print(distances[1])

# unpacking a function
miles, km = getDistance()
print(km)
