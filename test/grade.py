  
'''
Program: WAP to input marks of 5 subject and find average and assign grade.
Average Marks       Grade
90 & above           O
80 – 89              E
70-79                A
Below 70             B

'''
# Declarations
marks_list = []
total = 0.0; avg = 0.0

# Taking input from user
while True:
    for i in range(5):
        try:
            usr_inp = input("Please enter a marks: ")
            usr_inp = float(usr_inp)
            if usr_inp >= 0 and usr_inp <= 100:
                marks_list.append(usr_inp)
            else:
                print("Entered marks not in range of 0 and 100! Skipping this entry")
        except ValueError:
            print("Invalid data entered! Please enter a valid marks")
            break
    else:
        break

if len(marks_list) == 5:
    for i in range(5):
        total += marks_list[i]
    avg = total/len(marks_list)
    print(f"Average marks is {avg}")
    if avg >= 90:
        print("Grade is O")
    elif avg >= 80:
        print("Grade is E")
    elif avg >= 70:
        print("Grade is A")
    else:
        print("Grade is B")
else:
    print("Incomplete data provided!")