num = int(input("Enter a number to check if it is prime:"))
i=2
while i<= num/2:
    if num % i == 0:
        print(num, "is not a prime number")
        break
    i += 1
else:
    print(num, "is a prime number")
