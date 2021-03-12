'''
wap to calculate sum of first n numbers 1+2+...+n.
'''

n = int(input("Enter number: "))
s = 0
print(f"Sum of first {n} numbers is: ", end='')
for i in range(1, n+1):
    s = s + i
print(s)                                                                                                                                                                                                                                                                                                                                         