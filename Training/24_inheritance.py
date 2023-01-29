class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):  # Dog class inheriting the walk method from Mammal
    def bark(self):
        print('Bark!')


class Cat(Mammal):
    def meow(self):
        print('...meow')


Dog().walk()
Dog().bark()
Cat().walk()
