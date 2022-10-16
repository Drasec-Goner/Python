a = "Hello World"
b = "Soumya Manna"
sentence = "It's a me Mario"
print(a[6])
print(f"{b[7]}{b[5]}{b[9]}{b[9]}{b[8]}")
print(f"{b[0:4]}{b[1]}")
print(sentence[:])
print(sentence[-5:])
print(a[-5:-2])
print(sentence[:7])
print(len(a))
print(len(b))

if "Man" in b:
    print("Yes! It is there.")
else:
    print("No!")