# # Write a program to Convert decimal to Binary.
def binary(num):
    if(num>1):
        binary(num//2)
    print("The conversion of Decimal to Binary is",num%2,end="")

num=int(input("Enter the number:"))
binary(num)