  
'''
Program: Write a program to check whether the inputted number is prime or not
'''

def checkPrime(n):
    num = n
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

def main():
    inp = int(input("Enter a number to check prime: "))
    if inp > 1:
        checkPrime(inp)
    else:
        print("Invalid input given!")

if __name__ == "__main__":
    main()    