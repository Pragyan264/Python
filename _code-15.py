# Write a program to Check Armstrong number.
num=int(input("Enter the number:"))
arm=0
temp=num
r=0
while(temp!=0):
    r=temp%10
    arm=arm+(r**3)
    temp=temp//10
if(num==arm):
    print("The number is Armstrong number.")
else:
    print("The number is not Armstrong number.")