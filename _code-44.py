# Write a program to Write function to find factorial.
def Fact(x):
    f=1
    if(x==1 or x==0):
        print("The Factorial of a number is 1.")
    elif(x<0):
        print("The Factorial of negative number is not Posiible.")
    else:
        for i in range(1,x+1):
            f=f*i
        print("The Factorial of a number is",f)
x=int(input("Enter the number:"))
Fact(x)
