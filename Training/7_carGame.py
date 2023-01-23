print('What would you like to do with your car?\nhelp | start | stop | quit')
userInput = input('> ')
started = False

while userInput.lower() != 'quit':
    if userInput == 'start':
        if started:
            print('Car has already been started. Try a different command.')
        else:
            print('Car started')
            started = True
    elif userInput == 'stop':
        if not started:
            print('Car is already stopped. Try a different command.')
        else:
            print('Car stopped')
            started = False
    elif userInput == 'help':
        print('''
    start   - to start the car
    stop    - to stop the car
    quit    - to quit
        ''')
    else:
        print('I do not understand that command')

    userInput = input('> ').lower()
