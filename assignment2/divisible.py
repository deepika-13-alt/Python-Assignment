'''
Program: WAP to input a number and check whether the number is divisible by 5 and 3 or not.

'''
import re

inp = input("Enter a number: ")
regex_float = '[+-]?[0-9]+\.[0-9]+'
regex_int = "[-+]?[0-9]+$"
if re.search(regex_float, inp) or re.search(regex_int, inp):
    inp = float(inp)
    print("Checking whether the number is divisible by 5 and 3 or not.", end=' ')
    if inp % 5 == 0 and inp % 3 == 0:
        print(f"The number {inp} is divisible by 5 and 3")
    else:
        print(f"The number {inp} is NOT divisible by 5 and 3")
else:
    print("Entered input is not a number!")