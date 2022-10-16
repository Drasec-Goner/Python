# program to take input from user 
# if the length of the input is greater than 3 characters then add "ing" as suffix

wrd =input("Enter the input: ")
l = len(wrd)
if l > 3:
    print(wrd+"ing")
else:
    print(wrd)