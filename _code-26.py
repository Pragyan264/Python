# Write a program to Recursive Fibonacci.
def Fibo(num):
    if(num==1):
        return 0
    elif(num==2):
        return 1
    else:
        return Fibo(num-1)+Fibo(num-2)
num=int(input("Enter the number:"))
fibo=Fibo(num)
print("The Factorial at",num,"th number is",fibo)