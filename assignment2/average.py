'''
Program: WAP to determine a student’s final grade and indicate whether 
they are passing or failing. The final grade is calculated as the average of marks of four subjects.

'''

sub1 = float(input("Enter the marks of Subject 1: "))
sub2 = float(input("Enter the marks of Subject 2: "))
sub3 = float(input("Enter the marks of Subject 3: "))
sub4 = float(input("Enter the marks of Subject 4: "))

avg = (sub1+sub2+sub3+sub4)/4
if avg >= 40:
    print(f"Your Grade is: {avg}")
    print("Congratulations! You have passed!")
else:
    print(f"Your grade is: {avg}")
    print("Sorry! You failed!")