import calculations

result_add = calculations.add(10, 5)
print(result_add)

result_sub = calculations.subtract(10, 5)
print(result_sub)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print()

print(f"Sum: {add(num1, num2)}")
print(f"Difference: {subtract(num1, num2)}")
print(f"Product: {multiply(num1, num2)}")
print(f"Quotient: {divide(num1, num2)}")
