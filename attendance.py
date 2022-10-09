#program to find the attendance percentage of a student

name = input("Enter the name: ")
attn = int(input("Enter the days attended: "))
cllgDays = 360

attnPercent = (attn/cllgDays)*100

if attnPercent >= 75:
    print (name, " is able to give the test.")
    print ("Attendance Percentage: ", attnPercent)
else:
    print (name, " is not be able to give the test.")
    print ("Attendance Percentage: ", attnPercent)