# Write a program using match case that simulates a simple calculator.
# 1.Ask the user for two numbers and an operation (+, -, *, /).
# 2.Perform the operation using match case .
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operator=input("Enter the operator:")
match operator:
    case "+":
        print("The Sum of number is",num1+num2)
    case "-":
        print("The Subtraction of number is",num1-num2)
    case "*":
        print("The Multiplication  of number is",num1*num2)
    case "/":
        print("The Division of number is",num1/num2)
    case _:
        print("Something went Wrong!")