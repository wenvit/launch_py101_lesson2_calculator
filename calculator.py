####### Problem statement
# Ask the user for two numbers.
# Ask the user for the type of operation to perform:
# add, subtract, multiply or divide.
# Perform the calculation and display the result

# Refactoring
# 1. add prompt ==>
# 2. check that numbers and math operator inputs are valid

######## PEDAC
# inputs: 2 numbers, mathematical operation
# outputs: result of mathematical operation

# rules
# number inputs must strings capable of being converted to integers
# assume user won't input 0 as divisor
# must be capable of +, -, *, /

# test cases
# positive, negative values

# data structure
# convert input strings to float

# algorithm
# Define function `prompt` with a parameter `message`
#    `print` with f-string argument combining ==> with interpolated message
# Define function `invalid_number` with parameter `number`
#    try/except statement catches ValueError
#    if string input cannot be converted to integer
#    returns `True` if number is invalid
#    otherwise returns `False` if number is valid
# Ask user to input 2 numbers.
# Check that inputs are strings that can be converted to integers
# `while` loop continues iterating until `valid_input` returns False
#    each iteration asks user to input number
# Ask user preferred math operation: 1) '+', 2) '-', 3) '*', 4) '/'
# While loop that iterates as long as math operation entered is not one
#    of the valid choices
# Use match/case statement to find math operator entered,
#    and return result of that mathematical expression based
#    on the 2 numbers entered

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