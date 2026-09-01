# SYNET Technology - Data Science Internship
# Task 1: Simple Calculator

print("===== SIMPLE CALCULATOR =====")

num1 = float(input("Enter value of A: "))
num2 = float(input("Enter value of B: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid operator.")
