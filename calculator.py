# Internationalization

# Your calculator program is a hit, and it's being used all over the world!
# The problem is, not everyone speaks English. You now need to
# internationalize the messages in your calculator. You've already done the
# hard work of extracting all the messages to a configuration file.
# Now, all you have to do is send that configuration file to translators
# and call the right translation in your code.

# algorithm
# ask user to pick language preference: English, Spanish, French
# update calculator_messages.json to be nested dictionary to accommodate
# languages

import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

def string_to_int(number_str):
    return int(number_str)

prompt('''Please enter preferred language:
    English,
    Spanish, or
    French''')
language = input()

prompt(MESSAGES[language]['welcome'])

while True:

    prompt('Please enter 1st number:')
    num1 = input()

    while invalid_number(num1):
        prompt(MESSAGES[language]['invalid_num'])
        num1 = input()

    prompt('Enter 2nd number:')
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
            output = int(num1) + int(num2)
        case '2':  # represents subtraction
            output = int(num1) - int(num2)
        case '3':  # represents multiplication
            output = int(num1) * int(num2)
        case '4':  # represents division
            output = int(num1) / int(num2)

    prompt(f'The result is {output}')

    prompt(MESSAGES[language]['another'])
    user_response = input()

    if user_response and user_response[0].lower() != 'y':
        break