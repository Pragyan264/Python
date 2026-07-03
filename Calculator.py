# Basic Calculator
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operator=input("Enter the operaotor:")
if(operator=="+"):
    print("The sum of number is",num1+num2)
elif(operator=="-"):
    print("The subtraction of number is",num1-num2)
elif(operator=="*"):
    print("The multiplication of number is",num1*num2)
elif(operator=="/"):
    if(num2==0):
        print("Zero can't divide number")
    else:
        print("The Division of number is",num1/num2)
else:
    print("Something went wrong!")
