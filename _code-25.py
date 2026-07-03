# Write a program to Recursive factorial.
def Fact(num):
    if(num==1):
        return 0
    elif(num==2):
        return 1
    else:
        return Fact(num-1)+Fact(num-2)
num=int(input("Enter the number:"))
fact=Fact(num)
print("The Factorial at",num,"th number is",fact)