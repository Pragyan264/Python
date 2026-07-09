# Write a program to Write function to find maximum.
def Max(x,y,z):
    if(x>y and x>z):
        print("The maximum number between entered number is",x,".")
    elif(y>x and y>z):
        print("The maximum number between entered number is",y,".")
    elif(z>x and z>y):
        print("The maximum number between entered number is",z,".")
    elif((x==y) and y>z):
        print("The maximum number between entered number is",x,"and",y,".")
    elif((x==y) and z>x):
        print("The maximum number between entered number is",z,".")
    elif((z==y) and y>x):
        print("The maximum number between entered number is",z,"and",y,".")
    elif((z==y) and x>y):
        print("The maximum number between entered number is",x,".")
    elif((z==x) and x>y):
        print("The maximum number between entered number is",z,"and",x,".")
    elif((z==x) and x<y):
        print("The maximum number between entered number is",y,".")
    else:
        print("All number are equal.")

x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the third number:"))
Max(x,y,z)