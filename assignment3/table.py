'''
wap to generate a table of an inputted number using a loop.
'''

try:
  num = int(input("Enter an integer number: "))
  print("Enter integer number is : ",num)
  if num > 0:
      for i in range(1, 11):
          print(f"{num} * {i} = {num * i}")
  else:
      print(f"Entered number {num} is not a positive number")
except ValueError:
    print("Please input integer only...")