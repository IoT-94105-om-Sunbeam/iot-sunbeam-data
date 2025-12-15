def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Divide by Zero error"
    return a / b



def calculate(operand1, operand2, operation):
    return operation(operand1, operand2)

print("Addition:", calculate(50, 12, add))
print("Subtraction:", calculate(55, 14, subtract))
print("Multiplication:", calculate(256, 28, multiply))
print("Division:", calculate(1640, 4, divide))