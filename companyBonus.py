#Company will give bonus base for following criteria
#Time Spent in company     Bonus
# >10 years                  10%
# >=6 and <= 10               8%
# <6                          5%

#ask the salary and time spent from the user
#print the net bonus amount accordingly


user = input("Enter the name: ")
salary = int(input("Enter the salary: "))
time = int(input("Enter the time spent in company: "))

if time > 10:
    bonus = (10/100)*salary
    print("The net bonus amount of ",user, " : ", salary+bonus)
elif time >= 6 and time <=10:
    bonus = (8/100)*salary
    print("The net bonus amount of ",user, " : ", salary+bonus)
elif time < 6:
    bonus = (5/100)*salary
    print("The net bonus amount of ",user, " : ", salary+bonus)
else:
    print("You're FIRED :P")