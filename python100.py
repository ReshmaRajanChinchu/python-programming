a=input("enter the number")
if(a<=100000000000):
    b=len(a)
    i=0
    f=1
    while i<int(b):
        f=f*int(a[i])
        i+=1
    print(f)
