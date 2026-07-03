# Write a program to Convert decimal to binary. 
num=int(input("Enter the number:"))
b=bin(num)
b=b.replace("0b","")
print(b)