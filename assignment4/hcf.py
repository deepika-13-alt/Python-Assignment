'''
Program: Write a program to calculate highest common factor of two inputted integer.
'''
def hcf(x, y):  
    if x > y:  
       small = y  
    else:  
       small = x  
    for i in range(1, small + 1):  
        if((x % i == 0) and (y % i == 0)):  
            hcf = i  
    return hcf  
  
if __name__=="__main__":
    num1 = int(input("Enter first number: "))  
    num2 = int(input("Enter second number: "))  
    print("The H.C.F. of", num1,"and", num2,"is", hcf(num1, num2))  