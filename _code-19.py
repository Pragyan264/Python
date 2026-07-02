# Write a program to Print factors of a number
num=int(input("Enter thhe number:"))
print("The Factor of number is :")
for i in range(1,num+1):
    if(num%i==0):
        print(i)