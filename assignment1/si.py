'''
assignment-1
submitted by-Deepika Kumari Gupta

Q.Write a program to calculate simple interest for a given principal, rate of interest,and time. [Formula: I=P*t*i].
'''
principal = float(input("Enter the principal amount: "))

time = float(input("Enter the tenure in years: "))

rate = float(input("Enter the rate of interest % per annum: "))

si = principal*time*(rate/100)

print(f'''\nEntered principal = {principal}\n

Entered Rate of Interest = {rate}% p.a.\n

Entered Tenure = {time}\n

Calculated Interest = {si}''')
