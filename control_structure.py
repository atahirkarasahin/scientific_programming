#In this document is description control structure in Python

#Booleans & comparisons
a = "True" == "True"
print(a)

b = 2 != 3
print(b)

#Comparison
print(7 <= 5)

#If statements
a = 12
if a > 5:
    print("Result 3")
    if a < 7:
        print("Result 7")
        if a == 12:
            print("Result 12")

#else statements
a = 2
if a == 5:
    print("Number is 5")
else:
    if a == 11:
        print("Number is 11")
    else:
        if a == 7:
            print("Number is 7")
        else:
            print("Number isn't 5,7,11")

#elif statements
num = 7
if num == 5:
    print("Num is 5")
elif num == 7:
    print("Num is 7")
elif num == 11:
    print("Num is 11")
else:
    print("Num isn't 5,7,11")

#boolean logic (and, or, not)
x = 5
if x == 2 and x > 1:
    print("x=2 or x >1")
elif not x > 2:
    print("x not bigger than 2")
elif x < 3 or x >= 4:
    print("x bigger than 4")

if not True:
    print("True")

# operator precedence
print(2**2)
