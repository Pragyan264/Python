# Write a program to Count set bits in a number
num=int(input("Enter the number:"))
b=bin(num)
b=b.replace("0b","")
count=0
for i in range(0,len(b)):
    if(b[i]=="1"):
        count+=1
print("The Count set bits in a number",count)
