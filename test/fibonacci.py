'''
print fibonacci series >100.also print reverse fibonacci series.
'''

a = 0
b = 1
c = 0
l=[]
l.append(a)
l.append(b)
count = 1
while c <= 100 :
    l.append(c)
    count += 1
    a = b
    b = c
    c= a + b 
print("Original order")
for i in l:
    print(i, end=" ")
print()
print("Reverse Order ")
for i in l[::-1]:
    print(i, end=" ")                                                                          