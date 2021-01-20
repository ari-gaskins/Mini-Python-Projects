# Program that checks if number entered by the user is an Armstrong number
# Logic: user enters number, cpu iterates to find out how many digits are in the number, 
# cpu takes each number to the power of the number of digits, cpu adds these numbers together, 
# cpu then checks if sum matches original user number

# import math module for the sum method
import math

# get user input
num = input('enter a number: ')

# iterate through and count the number of characters
for n in range(len(num)):
    n + 1

# create the exponent based on the given number of characters
exponent = n + 1

# create a new empty list
str_digits = []

# place the string versions of the individual numbers into the empty list
for s in range(len(num)):
    str_digits.append(num[s])

# create another new empty list    
digits = []

# change the strings in the previous list into integers
# then place the new integers into the new list
for i in range(len(str_digits)):
    digits.append(int(str_digits[i]))

# create a new empty list
ex_digits = []

# calculate each number from the previous list to the power of the exponent
# then place the new values into the final new list
for d in range(len(digits)):
    ex_digits.append(digits[d] ** exponent)

# use the sum method to get the sum of all the numbers in the final list
armstrong = sum(ex_digits)  

# if statements to check if number is an armstrong number
if int(num) is armstrong:
    print('Congratulations! That is an Armstrong Number!')
if int(num) is not armstrong:
    print('Sorry! That is not an Armstrong Number.')