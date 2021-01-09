# Program that takes in an income amount and outputs the simple interest gained
# Logic: user inputs principal, interest rate, and term in years, cpu changes rate in decimal, cpu calculates the simple interest, 
# cpu outputs income, income after simple interest, and simple interest total

import math

# get user input 
principal = input('principal = $')
rate = input('rate (%) = ')
term = input('term (years) = ')

# change values into integers
principal = int(principal)
rate = int(rate)
term = int(term)

# change rate to decimal
rate = rate / 100

# calculate interest amount and principal after interest
interest = principal * rate * term 
total = principal + interest

# output results with 2 decimals of precision
print('Your principal is: $' + '%.2f'%principal)
print('Your simple interest total is: $' + '%.2f'%interest)
print('Your total after interest is: $' + '%.2f'%total)