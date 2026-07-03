# Write a program to Find x^n ** operator. 
num=int(input("Enter the number:"))
pow=int(input("Enter the power:"))
n=num
if(pow>0):
    for i in range(1,pow):
        n=n*num
    print(n)
elif(pow<0):
    pow=-pow
    for i in range(1,pow):
        n=n*num
    print(1/n)
else:
    print(1)