def addition(a,b):
    return int(a+b)

def subtraction(a,b):
    return int(a-b)

def multiplication(a,b):
    return float(a)*float(b)

def division(a,b):
    return int(a/b)

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = int(input("Enter Choice : "))

match choice:
    case 1:
        a = int(input("Enter num1 : "))
        b = int(input("Enter num2 : "))
        add = addition(a,b)
        print("Addition : ",add)
    case 2:
        a = int(input("Enter num1 : "))
        b = int(input("Enter num2 : "))
        sub = subtraction(a,b)
        print("Suntraction : ",sub)
    case 3:
        a = int(input("Enter num1 : "))
        b = int(input("Enter num2 : "))
        mul = multiplication(a,b)
        print("Multiplication : ",mul)
    case 4:
       a = int(input("Enter num1 : "))
       b = int(input("Enter num2 : "))
       div = division(a,b)
       print("Division : ",div)
