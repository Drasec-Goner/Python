#program to input check if the number is divisible by 2 and 3  or not

num = int(input("Enter the Number: "))

if num%2==0 & num%3==0:
    print(num,"is divisible by 2 and 3")
else:
    print(num, "is neither divisible by 2 nor 3")