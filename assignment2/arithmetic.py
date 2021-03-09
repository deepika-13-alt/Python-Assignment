'''
Program: WAP that reads two numbers and an arithmetic operator and displays the result.
'''

inp1 = float(input("Enter first number: "))
inp2 = float(input("Enter second number: "))
op = input("Enter the operation [+,-,*,/,%]: ")

if op in ['+', '-', '*', '/', '%']:
    if op == '+':
        result = inp1 + inp2
        print(f"Result of {op} is {result}")
    elif op == '-':
        result = inp1 - inp2
        print(f"Result of {op} is {result}")
    elif op == '*':
        result = inp1 * inp2
        print(f"Result of {op} is {result}")
    elif op == '/':
        if inp2 == 0:
            print("Division by 0 not allowed! Exiting...")
        else:
            result = inp1 / inp2
            print(f"Result of {op} is {result}")
    elif op == '%':
        result = inp1 % inp2
        print(f"Result of {op} is {result}")
else:
    print("Operator not defined! Please define operators as +,-,*,/,%")