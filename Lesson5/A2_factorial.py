def fact(n):
    if n ==0 or n==1:
        return 1
    else:
        return n * fact(n-1)

num = int(input("Enter the number to find factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("the factorial of", num, "is", fact(num))