# Write a program to Find GCD of two numbers.
def GCD(x,y):
    gcd=0
    if(x>y):
        for i in range(1,x+1):
            if(x%i==0 and y%i==0):
                gcd=i
        return gcd
    elif(y>x):
        for i in range(1,y+1):
            if(x%i==0 and y%i==0):
                gcd=i
        return gcd
    elif(x==y):
        return x
x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
gcd=GCD(x,y)
print("The GCD of two number is",gcd)
