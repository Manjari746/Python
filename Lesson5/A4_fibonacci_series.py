def fibo(n_terms):
    n1, n2 = 0, 1
    count = 0

    if n_terms <= 0:
        print("Please enter a positive integer.")
    elif n_terms == 1:
        print("Fibonacci sequence up to", n_terms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < n_terms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

num_terms = int(input("Enter the number of terms for Fibonacci series: "))
fibo(num_terms)