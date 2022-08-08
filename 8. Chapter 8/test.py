def summation(n) :
    if n == 1 :
        return 1
    return n + summation(n-1)

num = int(input("Enter the number : "))
a = summation(num)
print(f"The sum of first {num} natural numbers is {a}")