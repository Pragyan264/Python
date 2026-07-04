# Write a program to reverse number.
num=int(input("Enter the number:"))
rev=0
while(num!=0):
    rev=(rev*10)+(num%10)
    num//=10
print("The Reverse of number is",rev)