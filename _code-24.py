# Write a program to Find x^n ** operator. 
num=int(input("Enter the number:"))
pow=int(input("Enter the power:"))
n=num
if(pow>0):
    for i in range(1,pow):
        n=n*num
    print("The Solution of entered number is",n)
elif(pow<0):
    pow=-pow
    for i in range(1,pow):
        n=n*num
    print("The Solution of entered number is",1/n)
else:
    print("The Solution of entered number is 1")