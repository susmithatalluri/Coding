def calculator():
    print("Simple Calculator")
    
    # Prompt user to enter the first number
    num1 = float(input("Enter the first number: "))
    
    # Prompt user to enter the second number
    num2 = float(input("Enter the second number: "))
    
    # Prompt user to choose an operation
    print("Choose the operation you want to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Perform the chosen operation
    if operation == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operation choice.")

# Run the calculator
calculator()
