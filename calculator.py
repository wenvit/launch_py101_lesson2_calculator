####### Problem statement
# Ask the user for two numbers.
# Ask the user for the type of operation to perform: 
# add, subtract, multiply or divide.
# Perform the calculation and display the result

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
# Ask user to input 2 numbers.
# If valid inputs, convert input strings to float data type, else
#    ask user to input 2 valid numbers.
# Ask user preferred math operation: +, -, *, /
# Use match/case statement to find math operator entered, 
#    and return result of that mathematical expression based
#    on the 2 numbers entered

# code

print('Welcome to the Calculator!\n')

num1 = float(input('Please enter 1st number:\n'))
num2 = float(input('Enter 2nd number:\n'))

operation = input('''Pick a mathematical operation:\n 
    1) addition
    2) subtraction
    3) multiplication
    4) division\n  
''')

match operation:
    case '1':  # represents addition
        print(f'{num1} + {num2} = {num1 + num2}')
    case '2':  # represents subtraction
        print(f'{num1} - {num2} = {num1 - num2}')
    case '3':  # represents multiplication
        print(f'{num1} * {num2} = {num1 * num2}')
    case '4':  # represents division
        print(f'{num1} / {num2} = {num1 / num2}')
    case _:
        print('Please enter one of the choices.')
