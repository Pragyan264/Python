# Write a program to Print reverse pyramid.
#     *********
#      *******
#       *****
#        ***
#         *
a="*"
n=5
for i in range(5,0,-1):
    print(" "*(n-i),end="")
    print(a*(2*i-1))
    