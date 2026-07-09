# Write a program to Write function to check prime.
def prime(x):
    count=0
    if(x==1 or x==0 or x<0):
        print("The number is not a Prime.")
    else:
        for i in range(2,x):
            if(x%i==0):
                count=count+1
                break
        if(count>0):
            print("The number is not a Prime.")
        else:
            print("The number is a Prime.")
x=int(input("Enter the number:"))
prime(x)