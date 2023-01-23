highIncome = True
goodCredit = False
hasCriminalRecord = False

if highIncome and not hasCriminalRecord:
    print('Eligible for loan.')

name = 'Za'
if len(name) < 3:
    print('name must be at least 3 characters long')
elif len(name) > 50:
    print('Maximum characters for a name is 50')
else:
    print('Name looks good')