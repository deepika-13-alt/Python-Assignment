'''
Program: WAP to input a number and check whether the number is 2 digit number or not.

'''
import re

inp = input("Enter a number: ")
regex_float = '[+-]?[0-9]+ .[0-9]+' 
regex_int = "[-+]?[0-9]+$"
if re.search(regex_float, inp) or re.search(regex_int, inp):
    f_no = float(inp)
    s_no = int(f_no)
    c = 0
    diff = (f_no - s_no)
    if diff == 0:
        while f_no > 0:
            r = f_no % 10
            f_no = f_no // 10
            c+=1
    if c == 2:
        print(f"Entered number {inp} is a 2 Digit number")
    else:
        print(f"Entered number {inp} is not a 2 Digit number")
else:
    print("Entered input is not a number")