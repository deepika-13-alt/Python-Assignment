'''
wap to print your name 10 times.
'''


# Take input from user
name = input("Enter your name: ")

# Display input taken
print(f"Name entered by you: {name}")

# System message
print("Printing name ten times - ")
for i in range(10):
    print(name)