'''
Program: WAP to accept a character from the user and display whether it is a vowel or consonant.

'''

character = input("Enter any character to check vowel or consonant: ")
if character[0] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
    print(f"Entered character {character[0]} is a VOWEL!")
else:
    print(f"Entered character {character[0]} is a CONSONANT!")