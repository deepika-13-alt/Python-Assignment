  
'''
Create a set of 5 elements. Insert a new element in the set and delete an existing element from the set.
'''

my_set = {1, 2, 3, 4, 5}
print("Original set: ", my_set)

my_set.remove(5)
my_set.add(7)

print("Modified set: ", my_set)