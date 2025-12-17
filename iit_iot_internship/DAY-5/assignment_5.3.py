from geometry import area_of_circle as c
from geometry import area_of_rect as re

r=float(input("Enter radius:"))
l=float(input("Enter length:"))
b=float(input("Enter breadth:"))

print(f"Area of circle={c(r)}")
print(f"Area of Rectangle={re(l,b)}")
