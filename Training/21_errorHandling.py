while True:
    try:
        age = int(input('Age: '))
        income = 90000
        standing = income / age
        print(standing)
    except ZeroDivisionError:
        print('Age cannot be 0.')
    except ValueError:
        print('Please enter an integer')
