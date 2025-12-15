def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:
        return n * factorial(n - 1)
num=int(input("Enter number:"))
print("Factorial of 5:", factorial(num))
