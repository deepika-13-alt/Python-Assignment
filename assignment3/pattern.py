'''
wap to print the following patterns using loop.
 
    O       00000       1
   OOO       000        2   3
  OOOOO       0         4   5   6   
 OOOOOOO                7   8   9   10

'''
# Pattern 1
def tripatt1():
    num = int(input("enter the number of rows: "))
    for i in range(1, num+1):
        for j in range(1, num-i+1):
            print(end=" ")
        for j in range(i, 0, -1):
            print("O", end="")
        for j in range(2, i+1):
            print(0, end="")
        print()
# Pattern 2
def tripatt2():
    num = int(input("enter the number of rows: "))
    for i in range(num):
        for j in range(i):
            print(end=" ")
        for j in range(2*(num-i)-1):
            print("O", end="")
        print()
# Pattern 3
def tripatt3():
    num  = int(input("Enter a number: "))
    c = 1
    for row in range(1, num+1):
        for col in range(1, row+1):
            print(c, end=" ")
            c += 1
        print()
# Main script
if __name__ == '__main__':
    tripatt1()
    tripatt2()
    tripatt3()                                                   