'''
wap to display factors of an inputted number.
'''

num = int(input("Enter a number to find its factors: "))
print(f"Factors of {num} are: ")
for i in range(1, num+1):
    if num % i == 0:
        print(i, end=' ')