a1 = int(input("Enter 1st number : "))
a2 = int(input("Enter 2nd number : "))
a3 = int(input("Enter 3rd number : "))
a4 = int(input("Enter 4th number : "))
if a1 == a2 == a3 == a4 :
    print("Equal numbers!!!")
#break
if a1 > a2 :
    b = a1
else :
    b = a2

if a3 > a4 :
    c = a3
else :
    c = a4

if b>c :
    print("The greatest number is :",b)
else :
    print("The greatest number is :",c)



