#program to check whether the number is Armstrong or Not

num = int(input("Enter the Number: "))
b = len(str(num))
m = num
sum = 0

while(m != 0):
    r = m % 10
    sum = sum + (r ** b)
    m = m//10

if num == sum:
    print(num, " is an Armstrong Number.")
else:
    print(num, " is not an Armstrong Number.")