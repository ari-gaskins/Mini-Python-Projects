# Program that checks if number entered by the user is an Armstrong number
# Logic: user enters number, cpu iterates to find out how many digits are in the number, 
# cpu takes each number to the power of the number of digits, cpu adds these numbers together, 
# cpu then checks if sum matches original user number

import math

num = input('enter a number: ')

for n in range(len(num)):
    n + 1

exponent = n + 1

str_digits = []

for s in range(len(num)):
    str_digits.append(num[s])
    
digits = []

for i in range(len(str_digits)):
    digits.append(int(str_digits[i]))

ex_digits = []

for d in range(len(digits)):
    ex_digits.append(digits[d] ** exponent)

armstrong = sum(ex_digits)  

if int(num) is armstrong:
    print('Congratulations! That is an Armstrong Number!')
if int(num) is not armstrong:
    print('Sorry! That is not an Armstrong Number.')