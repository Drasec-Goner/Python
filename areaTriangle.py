#program to find the square root of a traingle

a = float(input('Enter the length of first side: '))  
b = float(input('Enter the length of second side: '))  
c = float(input('Enter the length of final side: '))

s = (a+b+c)/2

area = float((s*(s-a)*(s-b)*(s-c)) ** 0.5)

print("The Area of the triangle is: ", area)