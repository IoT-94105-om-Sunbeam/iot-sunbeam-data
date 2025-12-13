def is_prime(num):
    if num <= 1:
        return False 
    for i in range(2, num):
        if num % i == 0:
            return False 
    return True

first = int(input("Enter first number: "))
last = int(input("Enter last number: "))

print("Prime numbers in given range:")
for i in range(first, last + 1): 
    if is_prime(i):
        print(i,end=" ")