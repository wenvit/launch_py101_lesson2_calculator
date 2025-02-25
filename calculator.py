### Calculator with Bonus Features

import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

prompt('''Please enter preferred language:
    English,
    Spanish, or
    French''')
language = input()

prompt(MESSAGES[language]['welcome'])

while True:

    prompt('Please enter 1st number (int or float):')
    num1 = input()

    while invalid_number(num1):
        prompt(MESSAGES[language]['invalid_num'])
        num1 = input()

    prompt('Enter 2nd number (int or float):')
    num2 = input()

    while invalid_number(num2):
        prompt(MESSAGES[language]['invalid_num'])
        num2 = input()

    prompt('''Pick a mathematical operation:
        1) addition
        2) subtraction
        3) multiplication
        4) division''')
    math_op = input()

    while math_op not in ['1', '2', '3', '4']:
        prompt(MESSAGES[language]['invalid_op'])
        math_op = input()

    match math_op:
        case '1':  # represents addition
            output = float(num1) + float(num2)
        case '2':  # represents subtraction
            output = float(num1) - float(num2)
        case '3':  # represents multiplication
            output = float(num1) * float(num2)
        case '4':  # represents division
            output = float(num1) / float(num2)

    prompt(f'The result is {output:.1f}')

    prompt(MESSAGES[language]['another'])
    user_response = input()

    if user_response and user_response[0].lower() != 'y':
        break