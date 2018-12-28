a=int(input("enter the n"))
b=[]
e=int(input("enter the n to find nth smallest no"))
for i in range(0,a):
    c=int(input("enter the number"))
    b.append(c)
print(sorted(b)[e-1])
