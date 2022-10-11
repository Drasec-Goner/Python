#program to find the simple interest

p = float(input("Enter the Principal Amount: "))
t= int(input("Enter the time period: "))
r = float(input("Enter the rate of interest: "))

si = (p * t * r)/100

print("The simple interest is: ", si)