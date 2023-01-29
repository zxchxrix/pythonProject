# each key should be unique
customer = {
    'name': 'John Smith',
    'age': 30,
    'isVerified': True
}

print(customer['name'])

# get a default value for a non-existing key
print(customer.get('Birthday', 'Jan 1st, 1908'))

# updating values
customer['age'] = 31
print(customer['age'])

# adding keys
customer['car'] = 'BMW X5'
print(customer['car'])

print(customer)