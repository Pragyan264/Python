# Write a program to Convert decimal to Octal.
num=int(input("Enter the number:"))
o=oct(num)
o=o.replace("0o","")
print("The conversion of decimal to octal is",o) 