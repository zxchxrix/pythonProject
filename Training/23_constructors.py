class Point:
    def __init__(self, x, y):
        self.x = 10
        self.y = 20
    def move(self):
        print('move')
    def draw(self):
        print('draw')

point = Point(10, 20)
point.y = 11
print(point.y)

print('\n--Exercise--\n')

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'{self.name} is talking...')

person = Person('Zac')
person.talk()
