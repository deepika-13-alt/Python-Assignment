'''

Program: Write a program to merge two sorted array in another sorted array.

'''
def mergeSortedArray():
    sizeM = int(input("Enter the size of array 1: "))
    sizeN = int(input("Enter the size of array 2: "))
    arr1 = []; arr2 = []; res = []
    print("Taking input for ARRAY 1\n")
    for i in range(sizeM):
        inp = int(input("Enter element for array:"))
        arr1.append(inp)

    print("Taking input for ARRAY 2\n")
    for i in range(sizeN):
        inp = int(input("Enter element for array: "))
        arr2.append(inp)

    # Sorting the entered array
    for i in range(sizeM):
        for j in range(i+1, sizeM):
            if arr1[i]>arr1[j]:
                temp=arr1[i]
                arr1[i]=arr1[j]
                arr1[j]=temp

    for i in range(sizeN):
        for j in range(i+1, sizeN):
            if arr2[i]>arr2[j]:
                temp=arr2[i]
                arr2[i]=arr2[j]
                arr2[j]=temp

    print ("The original sorted array 1 is : " + str(arr1)) 
    print ("The original sorted array 2 is : " + str(arr2)) 

    size_1 = len(arr1) 
    size_2 = len(arr2) 
    res = [] 
    i, j = 0, 0
    
    while i < size_1 and j < size_2: 
        if arr1[i] < arr2[j]: 
            res.append(arr1[i]) 
            i += 1
    
        else: 
            res.append(arr2[j]) 
            j += 1
    res = res + arr1[i:] + arr2[j:] 
    # printing result 
    print ("The combined sorted list is : " + str(res)) 

def main():
    mergeSortedArray()

if __name__ == "__main__":
    main()