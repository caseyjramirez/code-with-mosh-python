
user_input = input();

while user_input != 'quit':
    if user_input == 'start':
        print('Car started')
        user_input = input();
    elif user_input == 'stop':
        print('Car stopped')
        user_input = input();
    elif user_input == 'help':
        print('''
        start - to start the car
        stop - to stop the car
        start - to exit the car
        ''')
        user_input = input();
    else:
        print('I dont understand this command...')
        user_input = input();