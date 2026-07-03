# Write a program to Find nth Fibonacci term.
a=0
b=1
num=int(input("enter the number:"))
print("The Fiboanacci series at",num,"is")
for i in range(1,num+1):
    if(i==num):
        print(a)
    x=a
    y=b
    z=x+y
    a=y
    b=z
    
