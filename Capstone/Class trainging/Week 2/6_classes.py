import random

class Student:
    def __init__(self, name, school_id, gpa=4):
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

    def __str__(self):
        return f'Student name: {self.name}, ID: {self.school_id}, GPA: {float(random.randint(0, self.gpa))}'


alex = Student('Alex', 12345)
print(alex.name)
print(alex.school_id)
print(alex)

michelle = Student('Michelle', 453255)
print(michelle)

print('--\n--')


class Author():
    def __init__(self, name):
        self.alies = name
        self.books_list = []

    def publish(self, book_title):
        self.books_list.append(book_title)

    def __str__(self):
        book_list = ', '.join(self.books_list) or 'No books'
        # if self.books_list:
        #     book_list = ', '.join(self.books_list)
        # else:
        #     book_list = 'No books'
        return f'Author: {self.alies} \n- Books: {book_list}'


jkRowling = Author('J.K. Rowling')
jkRowling.publish('Harry Potter 1')
jkRowling.publish('Harry Potter 2')
print(jkRowling)

zac = Author('Zacharia')
print(zac)