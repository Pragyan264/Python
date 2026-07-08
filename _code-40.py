# Write a program to Print character pyramid.
#        A
#       ABA
#      ABCBA
#     ABCDCBA
#    ABCDEDCBA
n=5
for i in range(65,70):
    print(" "*(65+n-i-1),end="")
    for j in range(65,i+1):
        print(chr(j),end="")
    for k in range(i-1,64,-1):
        print(chr(k),end="")
    print()