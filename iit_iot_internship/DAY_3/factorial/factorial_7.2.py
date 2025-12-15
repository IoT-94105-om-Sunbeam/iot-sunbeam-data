def power(base, exp):
    if exp == 0:         
        return 1
    else:
        return base * power(base, exp - 1)
base=int(input("Enter base:"))
exp=int(input("Enter exponent:"))
print("2 power 4:", power(base, exp))