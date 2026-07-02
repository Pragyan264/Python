# Write a program to Check strong number
num=int(input("Enter the number:"))
temp=num
r=0
fact=1
strong=0
while(temp!=0):
    r=temp%10
    for i in range (1,r+1):
        fact=fact*i
    temp=temp//10 
    strong=strong+fact
    fact=1
if(num==strong):
    print("The number is strong number.")
else:
    print("The number is not strong number.")
