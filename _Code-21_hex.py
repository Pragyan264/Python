# Write a program to Convert decimal to hexadecimal.
num=int(input("Enter the number:"))
h=hex(num)
h=h.replace("0x","")
print("The conversion of decimal to hexdecimal is",h)