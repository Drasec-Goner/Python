#take input of age from 3 people
#determine the oldest and youngest

firstPerson = int(input("Enter the age of First person: "))
secondPerson = int(input("Enter the age of Second person: "))
thirdPerson = int(input("Enter the age of Third person: "))

if firstPerson > secondPerson and firstPerson > thirdPerson:
        print("First Person is Oldest")
elif secondPerson > thirdPerson and secondPerson > firstPerson:
        print("Second Person is Oldest")
elif secondPerson < thirdPerson and thirdPerson > firstPerson:
    print("Third person is Oldest")

if firstPerson < secondPerson and firstPerson < thirdPerson:
        print("First Person is Youngest")
elif secondPerson < thirdPerson and secondPerson < firstPerson:
        print("Second Person is Youngest")
elif secondPerson > thirdPerson and thirdPerson < firstPerson:
    print("Third person is Youngest")
else:
    print("Every Person has same age")