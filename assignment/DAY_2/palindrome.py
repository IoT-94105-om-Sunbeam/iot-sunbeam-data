n1=int(input("enter a 5 digit number:"))
d1=n1%10
d2=(n1//10)%10
d3=(n1//100)%10
d4=(n1//1000)%10
d5=(n1//10000)
if d1==d5 and d2==d4:
    print("palindrome")
else :
    print("not palindrome")


