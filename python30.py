a=input("enter the time")
b=input(" enter the time to subtract ")
c=a.split(" ")
d=b.split(" ")
e=(int(c[0])*60)+int(c[1])
f=(int(d[0])*60)+int(d[1])
v=e-f
j=v//60
k=v%60
print(str(j)+":"+str(k))
