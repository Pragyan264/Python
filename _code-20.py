# Write a program to Find largest prime factor.
num=int(input("Enter the number:"))
ans=0

for i in range(2,int(num**(1/2))+1):
    if(num%i==0):
        ans=i
        while(num%i==0):
            num//=i
if(num>1):
    ans=num
print("The largest Prime factor of number is",ans)

