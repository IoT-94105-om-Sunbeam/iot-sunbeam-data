from random import choice


num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
print("1.addition")
print("2.subtraction")
print("3.division")
print("4.multiplication")
choice=int(input("enter your choice:"))
match choice :
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1/num2)
    case 4:
        print(num1*num1)
        