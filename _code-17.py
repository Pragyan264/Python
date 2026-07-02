# Write a program to Check perfect number. 
num=int(input("Enter the number:"))
sum=0
temp=num
for i in range(1,num):
    if(temp%i==0):
        sum=sum+i
if(num==sum):
    print("The number is Perfect number.")
else:
    print("The number is not Perfect number.")