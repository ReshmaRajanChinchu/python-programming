a=int(input("enter the n"))
b=[]
e=int(input("enter the n to find odd"))
for i in range(0,a):
    c=int(input("enter the number"))
    if(c%2==1):
        b.append(c)
print(b[e-1])
