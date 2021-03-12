'''
Program: Write a program to check whether the inputted number is palindrome or not.

'''

def checkPalin(num):
    temp = num; sum = 0
    while temp > 0:
        rem = temp % 10
        sum = sum * 10 + rem
        temp = temp // 10
    
    if sum == num:
        return True
    else:
        return False

def main():
    inp = int(input("Enter any number to check palindrome: "))
    if inp > 0:
        if checkPalin(inp):
            print(f"Entered number {inp} is a Palindrome number")
        else: 
            print(f"Entered number {inp} is not a Palindrome number")
    else:
        print("Invalid input given!")

if __name__ == "__main__":
    main()