# Write a program that takes a number from the user and prints “Even” if it is
# even, otherwise “Odd”.
num=int(input("Enter the number:"))
if(num==0):
    print("THe entered number is neither odd nor even.")
elif(num%2==0):
    print("The entered number is even.")
else:
    print("The entered number is odd.")