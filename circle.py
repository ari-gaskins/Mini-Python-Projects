# Program that calculates the area of a circle 
# Logic: user enters the radius, cpu calculates area of a circle based on given radius, cpu outputs the area

# import the math module to access pi
import math

# get radius
radius = input('enter a radius: ')

# make the radius an integer
radius = int(radius)

# calculate the area of a circle
area = math.pi * (radius ** 2)

# output area with 2 decimal places of precision
print('%.2f'%area)