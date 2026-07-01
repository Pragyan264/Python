# Write a program to Find LCM of two numbers.
def LCM(x,y):
    lcm=0
    c=1
    if(x>y):
        lcm=x
    else:
        lcm=y
    while(c==1):
        if(lcm%x==0 and lcm%y==0):
            c=0
        else:
            lcm+=1
    return lcm
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
lcm=LCM(x,y)
print("The LCM of two number is",lcm)