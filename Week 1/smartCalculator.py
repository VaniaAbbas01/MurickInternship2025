# addition
def sum(a,b):
    return a+b

# subtraction
def difference(a,b):
    return a-b

# product
def product(a,b):
    return a*b

# division
def division(a,b):
    if (b > 0):
        return a/b
    print("Error: Division by zero is not allowed.")
    return

# exponentiation
def exp(a,b):
    return a ** b

# modulus
def mod(a,b):
    if (b > 0):
        return a % b
    print("Error: Modulus by zero is not allowed.")
    return

# calculator
def calculator():
    try:
        # Take user input
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /, **, %): ")
        num2 = float(input("Enter the second number: "))

        # Perform calculation
        if operator == "+":
            result = sum(num1,num2)
        elif operator == "-":
            result = difference(num1,num2)
        elif operator == "*":
            result = product(num1,num2)
        elif operator == "/":
            result = division(num1,num2)
        elif operator == "**":
            result = exp(num1,num2)
        elif operator == "%":
            result = mod(num1,num2)
        else:
            print("Error: Invalid operator.")
            return

        # Display result in required format
        print(f"{num1} {operator} {num2} = {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")

calculator()
