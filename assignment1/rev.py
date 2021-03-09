'''
Q. If two digit number is input through the keyboard. Write a program to reverse the number.
'''

num = int(input("Enter any number to reverse: "))

orig_no = num

s = 0

while num > 0 :

    r = num % 10

    s = s*10 + r

    num = num // 10

print(f"Original number is {orig_no}\nReversed number is {s}")
 