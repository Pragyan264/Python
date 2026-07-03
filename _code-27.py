# Write a program to Recursive sum of digits.
def sum_digit(num):
   
    
    
    if(num==0):
        return 0
    else:
        return num%10+(sum_digit(num//10))
    
num=int(input("Enter the number:"))
digit=sum_digit(num)
print("The sum of digit is",digit)