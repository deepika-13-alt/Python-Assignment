'''
 Write a program to calculate average marks of five inputted marks.

'''
marks_data = []
sub_count = 5;
def getData():
    for i in range(sub_count):
        inp = float(input("Enter the marks: "))
        if 0<=inp<=100:
            marks_data.append(inp)
        else:
            print("Invalid marks entered")

def calData():
    l_marks_data = len(marks_data)
    calc = 0;
    if l_marks_data == 5:
        for i in marks_data:
            calc = calc + i
        print(f"Average of marks entered is: {calc/l_marks_data}")
    else:
        print("Insufficient list of marks!")

if __name__ == "__main__":
    getData()
    calData()
    