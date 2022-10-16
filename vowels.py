#program to take input from user

vowels = ["A","E","I","O","U","a","e","i","o","u"]

wrd = str(input("Enter a letter: "))

if wrd in vowels[:]:
    print("It's a Vowel.")
else:
    print("It's not a Vowel.")