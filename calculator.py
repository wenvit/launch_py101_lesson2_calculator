####### Problem statement
# Ask the user for two numbers.
# Ask the user for the type of operation to perform:
# add, subtract, multiply or divide.
# Perform the calculation and display the result

# Refactoring
# 1. add prompt ==>

######## PEDAC
# inputs: 2 numbers, mathematical operation
# outputs: result of mathematical operation

# rules
# assume valid numbers are entered
# also assume user won't input 0 as divisor
# must be capable of +, -, *, /

# test cases
# positive, negative values

# data structure
# convert input strings to float

# algorithm
# Define function `prompt` with a parameter `message`
#    `print` invocation with f-string argument combining
#    ==> with message
# Ask user to input 2 numbers.
# If valid inputs, convert input strings to float data type, else
#    ask user to input 2 valid numbers.
# Ask user preferred math operation: +, -, *, /
# Use match/case statement to find math operator entered,
#    and return result of that mathematical expression based
#    on the 2 numbers entered

# code

def prompt(message):
    print(f'==> {message}')


prompt('Welcome to the Calculator!')

prompt('Please enter 1st number:')
num1 = float(input())
prompt('Enter 2nd number:')
num2 = float(input())

prompt('''Pick a mathematical operation:
    1) addition
    2) subtraction
    3) multiplication
    4) division\n  
''')
math_op = input()

match math_op:
    case '1':  # represents addition
        prompt(f'{num1} + {num2} = {num1 + num2}')
    case '2':  # represents subtraction
        prompt(f'{num1} - {num2} = {num1 - num2}')
    case '3':  # represents multiplication
        prompt(f'{num1} * {num2} = {num1 * num2}')
    case '4':  # represents division
        prompt(f'{num1} / {num2} = {num1 / num2}')
    case _:
        prompt('Please enter one of the choices.')
