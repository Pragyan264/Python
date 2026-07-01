# Write a program to Generate Fibonacci series
a=0
b=1
x=a
y=b
print("The finonacci series is")
for i in range(1,8):
    x=a
    y=b
    z=x+y
    a=y
    b=z
    print(x)
