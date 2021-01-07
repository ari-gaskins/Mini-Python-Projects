# Program that finds the max between two numbers inputted by the user
# Logic: user inputs two numbers, cpu compares two numbers, if a is greater than b, cpu outputs 'a > b'
# if a is less than b, cpu outputs 'a < b'

# get user input
a = input('a = ')
b = input('b = ')

# change strings to ints
a = int(a)
b = int(b)

# compare numbers, output results
if a > b:
    print('a > b')
if a < b:
    print('a < b')