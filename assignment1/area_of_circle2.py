'''
Q.Write a program to calculate area of a circle and input for radius through keyboard.
'''

import math
radius = float(input("Please enter the radius of the circle: "))
area = math.pi * (radius ** 2)
print(f"Area of circle for radius {radius} is {area}")
