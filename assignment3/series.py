'''
wap to print this series.
Enter the range: 20
1 3 5 7 9 11 13 15 17 19
'''
n = int(input("Range: "))

for i in range(1, n+1, 2):
    print(i, end=" ")