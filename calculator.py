#### Problem statement

# Asking the user for another calculation

# Currently, our calculator asks the user for two
# numbers and an operation and then exits after displaying
#  the result. Wouldn't it be nice if we could ask
# the user if they wanted to perform another calculation
# and start a new calculation when they respond with yes?

# algorithm
# Add `while True:` loop that starts before prompt to enter 1st number
#   and encloses rest of code.
# After printing result of calculator, ask user if they'd like
#   perform another calculation. If user inputs `no`, break

# code
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

prompt('Welcome to the Calculator!')

while True:

    prompt('Please enter 1st number:')
    num1 = input()

    while invalid_number(num1):
        prompt('The number must be an integer. Try again')
        num1 = input()

    prompt('Enter 2nd number:')
    num2 = input()

    while invalid_number(num2):
        prompt("Hmmm...that isn't a valid integer. Try again")
        num2 = input()

    prompt('''Pick a mathematical operation:
        1) addition
        2) subtraction
        3) multiplication
        4) division  
    ''')
    math_op = input()

    while math_op not in ['1', '2', '3', '4']:
        prompt('You must choose 1, 2, 3, or 4')
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

    prompt('Would you like to perform another calculation?')
    user_response = input()

    if user_response and user_response[0].lower() != 'y':
        break