#program to make a Calculator

num1 = float(input("Enter the 1st Number: "))
num2 = float(input("Enter the 2nd Number: "))
opr =  input("Enter the operator: ")

if opr == "+":
    print(num1+num2)
elif opr == "-":
    print(num1-num2)
elif opr == "*":
    print(num1*num2)
elif opr == "/":
    print(num1/num2)
elif opr == "**":
    print(num1**num2)
elif opr == "%":
    print(num1%num2)
elif opr == "//":
    print(num1//num2)
else:
    print("Not a valid operator!")