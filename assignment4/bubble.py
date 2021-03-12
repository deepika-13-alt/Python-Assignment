'''
Program: Write a program to sort all the elements in ascending order using bubble sort

'''
def bubbleSort():
    arr1 = []
    size = int(input("Enter the size of array: "))
    print("Taking input for ARRAY\n")
    for i in range(size):
        inp = int(input("Enter element for array: "))
        arr1.append(inp)

    # Sorting the entered array
    i, j = 0, 0
    for i in range(size):
        for j in range(i+1, size):
            if arr1[i]>arr1[j]:
                temp=arr1[i]
                arr1[i]=arr1[j]
                arr1[j]=temp

    print ("The sorted array is : " + str(arr1)) 
    
def main():
    print("Implementing Bubble sort with list")
    bubbleSort()

if __name__ == "__main__":
    main()