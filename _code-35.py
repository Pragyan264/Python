# Write a program to Print repeated character
# pattern.
# A
# BB
# CCC
# DDDD
# EEEEE
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end="")
    print()