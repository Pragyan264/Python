# Write a program to Write function to find factorial.
import math
x=int(input("Enter the number:"))
if(x>=0):
    Fact=math.factorial(x)
    print("The Factorial of a number is",Fact,".")
else:
    print("The Factorial of negative number is not possible.")