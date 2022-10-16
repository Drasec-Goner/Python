#program to input length of 3 sides and check whether traingle can be formed or not

s1 = int(input("Enter the length of 1st side: "))
s2 = int(input("Enter the length of 2nd side: "))
s3 = int(input("Enter the length of 3rd side: "))

if s1+s2 >s3 and s2+s3>s1 and s1+s3>s2:
    print("Triangle is Valid.")
else:
    print("Triangle is not valid.")