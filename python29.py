a=int(input("enter the time"))
s=0
if(a<=60):
    print(str(s)+":"+ str(a))
else:
    c=a//60
    d=a%60
    print(str(c)+":"+str(d))

