'''
Program: WAP to input 3 numbers and find the second smallest.

'''
import re

# Declarations
regex_float = '[+-]?[0-9]+\.[0-9]+'
regex_int = "[-+]?[0-9]+$"
small_list = []
small_1 = 0
small_2 = 0
# Taking input from users
print("Enter 3 numbers for finding smallest among them")
for i in range(3): 
    inp = input("Enter any number to insert: ")  
    if re.search(regex_float, inp):
        inp = float(inp)
        small_list.append(inp)
    elif re.search(regex_int, inp):
        inp = int(inp)
        small_list.append(inp)
    else:
        print("Invalid data entered!")
        break

# Processing data
if len(small_list) == 3:
    for item in small_list[1:]:
        if item < small_1:
            small_2 = small_1
            small_1 = item
        elif small_2 == 0 or small_2 > item:
            small_2 = item
    # Display output
    print("The entered elements are: ", end=" ")
    for item in small_list:
        print(item, end=" ")
    print(f"and, the second smallest number is: {small_2}")
else:
    print("Unable to compute data! Insufficient data received!")