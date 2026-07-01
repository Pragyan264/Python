# Write a program to Print Armstrong numbers in a range
num1=int(input("Enter the initial number:"))
num2=int(input("Enter the final number:"))
temp=0
arm=0
r=0
for i in range(num1,num2+1):
    temp=i
    while(temp!=0):
        r=temp%10
        arm=arm+(r**3)
        temp=temp//10
    if(i==arm):
        print("The number",i,"is Armstrong number.")
    arm=0