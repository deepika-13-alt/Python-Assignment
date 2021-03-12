'''
Find the sum of Fibonacci series up to a given range inputted by use.

'''

def printFibonacciNumbers():
    num = int(input("Enter range to print Fibonacci series: "))
    t1 = 0; t2 = 1; nextTerm = 0;
    lFibo = []
    lFibo.append(t1)
    lFibo.append(t2)
    nextTerm = t1+t2
    while nextTerm <= num:
        lFibo.append(nextTerm)
        t1 = t2
        t2 = nextTerm
        nextTerm = t1 + t2
    sum = 0
    for i in lFibo:
        sum += i
    print(f"Sum of {num} fibonacci is {sum}")

def main():
    printFibonacciNumbers()

if _name_ == "_main_":
    main()  