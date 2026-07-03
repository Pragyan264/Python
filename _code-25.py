# Write a program to Recursive factorial.
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
num=int(input("Enter the number:"))
Fact=fact(num)
print("The Factorial of number is",Fact)