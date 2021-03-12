'''
Program: WAP to input 3 side of a triangle and prints its type (i.e Equilateral/Isosceles/Scalene).

'''
# Declarations
sides_list = []
i = 3
# Take input from user
while True:
    while i > 0:
        try:
            usr_inp = input("Enter the side of a triangle: ")
            usr_inp = float(usr_inp)
            i = i - 1
            if usr_inp >= 0 and usr_inp <= 60:
                sides_list.append(usr_inp)
            else:
                print("Entered input is out of range [0 - 60]. Discarded the input")
        except ValueError:
            print("Entered input is not valid! Please re-enter")
            break
    else:
        break

# Processing data
if len(sides_list) == 3:
    if sides_list[0] == sides_list[1] == sides_list[2]:
        print("The triangle is Equilaterial")
    elif sides_list[0] == sides_list[1] or sides_list[1] == sides_list[2] or sides_list[2] == sides_list[0]:
        print("The triangle is Isosceles")
    else:
        print("The triangle is Scalene")
else:
    print(f"Sides of triangle received is {len(sides_list)}. Hence, unable to display appropriate result!")