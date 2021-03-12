  
'''
Write an expression that changes the first item in a tuple. (4, 5, 6) should become (1, 5, 6) in the process.
T1=(4,5,6)
T1=(1,5,6)
'''

T1 = (4, 5, 6)
print("Original Tuple: ", T1)
l1 = list(T1)
l1[0] = 1
T1 = tuple(l1)
print("Modified Tuple: ", T1)