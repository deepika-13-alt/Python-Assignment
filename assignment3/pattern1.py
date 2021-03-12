'''
wap to print the following using loop.
*       AAA     AAAAA
**      AA       AAAA
***     A         AAA 
****               AA
                    A

'''
# Pattern 1
def pattern1():
    num = int(input("Enter a number: "))
    for row in range(1, num+1):
        for col in range(1, row+1):
            print('*', end='')
        print()
# Pattern 2
def pattern2():
    num = int(input("Enter a number: "))
    for row in range(num+1, 1, -1):
        for col in range(1, row):
            print("A", end='')
        print()
# Pattern 3
def pattern3():
    num = int(input("Enter a number: "))
    for i in range (num, 0, -1): 
        print((num-i) * ' ' + i * 'A') 

# Main script
if __name__=="__main__":
    pattern1()
    pattern2()
    pattern3()
