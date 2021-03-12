'''
wap to display all the prime no upto n.
'''

prime = int(input("Enter the number: "))

print(f"Prime numbers upto {prime} are: ")

for num in range(2, prime+ 1):
    if num > 1:
       for i in range(2, num):
           if num % i == 0:
               break
       else:
           print(num, end=" ")