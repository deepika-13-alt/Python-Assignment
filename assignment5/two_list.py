  
'''
Concatenate two lists in the following order
Input: L1=[1,2]L2=[4,5]
Output: L3=[(1,4),(1,5),(2,4),(2,5)]
'''


l1 = [1,2]
l2 = [4,5]
print("Original list 1: ", l1)
print("Original list 2: ", l2)
l3 = []
for i in l1:
    for j in l2:
        tup = (i,j)
        l3.append(tup)
print("Output: ", l3)