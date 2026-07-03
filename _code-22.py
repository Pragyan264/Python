# Write a program to Convert binary to decimal. 
num=int(input("Enter the numeber:"))
dec, i=0,0
while(num>0):
    r=num%10
    exp=r*(2**i)
    dec=dec+exp
    i+=1
    num//=10
print("The conversion of Binary to Decimal is",dec)