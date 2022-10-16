a = 5
b = 10
c = 20
d = 90
string = "A: {2}, B: {0}, C: {1}"
string1 = "A: {2}, B: {1}, C: {3} : {0}"
print(string.format(a,b,c))
print(string1.format(a,b,c,d))