'''
Program: Write a program using function to determine whether a number is a perfect number. A natural number is said to be
a perfect number if it is the sum of its divisors. [6=1+2+3]
'''

def checkPerfect(num):
    list_divisor = []
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            list_divisor.append(i)

    for i in list_divisor:
        sum = sum + i

    if sum == num:
        return True
    else:
        return False

def main():
    inp = int(input("Enter any number to check whether it is perfect or not: "))
    result = checkPerfect(inp)
    if result:
        print(f"Entered number {inp} is perfect number!")
    else:
        print(f"Entered number {inp} is not perfect number!")

if __name__ == "__main__":
    main()