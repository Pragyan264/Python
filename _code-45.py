# Write a program to Write function for palindrome.
def palin(x):
    temp=x
    rev=0
    if(x>=0):
        while(temp>0):
            rev=(rev*10)+temp%10
            temp//=10
        if(x==rev):
            print("The entered number is Palindrome.")
        else:
            print("The entered number is not a Palindrome.")
    else:
        print("The negative number are not considered as Palindrome.")
x=int(input("Enter the number:"))
palin(x)