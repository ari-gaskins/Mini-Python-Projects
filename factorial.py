# Program that computes the factorial of a given number
# Logic: user inputs a number, cpu computes factorial using math module method, cpu outputs factorial of the number

# import math module
import math

# get user input
a = input('a = ')

# change user input into integer
a = int(a)

# get factorial of user input
a_fact = math.factorial(a)

# output the factorial
print(f'a! = {a_fact}')

