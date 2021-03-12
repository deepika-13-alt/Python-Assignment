'''
Program: Write a program that prints Armstrong number s in the range 1 to 1000.

'''

def checkArmstrong():
    print("Printing armstrong number in the range of 1-1000")
    for i in range(1, 1001):
        sum = 0
        temp = i
        f_no = i
        c = 0
        while f_no > 0:
            r = f_no % 10
            f_no = f_no // 10
            c+=1
        while temp > 0:
            digit = temp % 10
            sum += digit ** c
            temp //= 10

        if i == sum:
            print(i,"is an Armstrong number")

def main():
    checkArmstrong()

if __name__ == "__main__":
    main()