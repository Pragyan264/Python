# Write a program to Print star pyramid.
#          *
#         ***
#        *****
#       *******
#      *********
a="*"
n=5
for i in range(1,6):
    print(" "*(n-i),end="")
    print(a*(2*i-1))
    