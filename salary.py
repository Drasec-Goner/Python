# A company decided to give bonus of Rs 1000 to employee if his/her service is more than 5 years 
#Ask user their salary and year of service and print the net bonus amount

user = input("Enter the user name: ")
salary = int(input("Enter the salary: "))
year_service = int(input("Enter the years of service: "))

print("The user name: ", user)

if year_service > 5:
    salary += 1000
    print("The net bonus amount is: ", salary)
else:
    print("The net bonus amount is: ", salary)