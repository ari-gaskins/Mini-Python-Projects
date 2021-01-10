# Program that takes in an income amount and outputs the compound interest gained
# Logic: user inputs principal, interest rate, and term in years, cpu changes rate in decimal, cpu calculates the compound interest, 
# cpu outputs income, income after compound interest, and compound interest total

import math

# get user input 
principal = input('principal = $')
rate = input('rate (%) = ')
num = input('number of times compounded per year = ')
term = input('term (years) = ')

# change values into integers
principal = int(principal)
rate = int(rate)
term = int(term)
num = int(num)

# change rate to decimal
rate = rate / 100

# calculate interest amount and principal after interest
interest = principal * (1 + (rate / num))**(num * term)
total = interest + principal

# output results with 2 decimals of precision
print('Your principal is: $' + '%.2f'%principal)
print('Your simple interest total is: $' + '%.2f'%interest)
print('Your total after interest is: $' + '%.2f'%total)